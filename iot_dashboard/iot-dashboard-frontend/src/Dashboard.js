import { io } from "socket.io-client";
import React, { useEffect, useState } from "react";

// Function to send commands to the backend
async function sendCommand(device, command) {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/control", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        device: device,
        command: command,
      }),
    });

    if (!response.ok) throw new Error("Failed to send command");
    const result = await response.json();
    console.log(result.message);
  } catch (error) {
    console.error("Error sending command:", error);
  }
}

export default function Dashboard() {
  const [isConnected, setIsConnected] = useState(false);
  const [led1State, setLed1State] = useState(false); // LED1 on/off state
  const [led2State, setLed2State] = useState(false); // LED2 on/off state
  const [servo1State, setServo1State] = useState(false); // Servo1 on/off state
  const [servo2State, setServo2State] = useState(false); // Servo2 on/off state
  const [led1Color, setLed1Color] = useState([1023, 0, 0]); // LED1 color
  const [led2Color, setLed2Color] = useState([1023, 0, 0]); // LED2 color
  const [servo1Angle, setServo1Angle] = useState(0); // Servo1 angle
  const [servo2Angle, setServo2Angle] = useState(0); // Servo2 angle

  useEffect(() => {
    const socket = io("http://127.0.0.1:5000", {
      transports: ["websocket"], // Enforce WebSocket-only transport
    });

    socket.on("connect", () => {
      console.log("Connected to Flask-SocketIO");
      setIsConnected(true); // Update connection status
    });

    socket.on("disconnect", () => {
      console.log("Disconnected from Flask-SocketIO");
      setIsConnected(false); // Update connection status
    });

    return () => {
      socket.disconnect(); // Cleanup on component unmount
    };
  }, []);

  // Toggle LED on/off
  const toggleLed = (led, state, color) => {
    const newState = !state;
    const action = newState ? "on" : "off";
    sendCommand(led, { action, color: action === "on" ? color : [0, 0, 0] });
    led === "LED1" ? setLed1State(newState) : setLed2State(newState);
  };

  // Toggle Servo on/off
  const toggleServo = (servo, state, angle) => {
    const newState = !state;
    const action = newState ? "move" : "stop";
    sendCommand(servo, {
      action,
      start_angle: 0,
      end_angle: action === "move" ? angle : 0,
    });
    servo === "servo1" ? setServo1State(newState) : setServo2State(newState);
  };

  // Update LED color and send command
  const handleLedChange = (led, color) => {
    setLed1Color(led === "LED1" ? color : led1Color);
    setLed2Color(led === "LED2" ? color : led2Color);
    sendCommand(led, { action: "on", color });
  };

  // Update servo angle and send command
  const handleServoMove = (servo, angle) => {
    if (servo === "servo1") setServo1Angle(angle);
    else setServo2Angle(angle);

    sendCommand(servo, { action: "move", start_angle: 0, end_angle: angle });
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center">IoT Device Dashboard</h1>
      <h4 className="text-center">
        ESP32 Connection Status:{" "}
        <span style={{ color: isConnected ? "green" : "red" }}>
          {isConnected ? "Connected" : "Disconnected"}
        </span>
      </h4>

      <div className="row">
        {/* LED Controls */}
        <div className="col-md-6">
          <h2>LED Controls</h2>

          {/* LED 1 Control */}
          <div className="card mb-3">
            <div className="card-header">
              LED 1
              <button
                className="btn btn-sm btn-primary float-end"
                onClick={() => toggleLed("LED1", led1State, led1Color)}
              >
                {led1State ? "Turn Off" : "Turn On"}
              </button>
            </div>
            <div className="card-body">
              {["Red", "Green", "Blue"].map((color, index) => (
                <div className="mb-3" key={color}>
                  <label>{color}</label>
                  <input
                    type="range"
                    min="0"
                    max="1023"
                    value={led1Color[index]}
                    onChange={(e) => {
                      const newColor = [...led1Color];
                      newColor[index] = parseInt(e.target.value);
                      handleLedChange("LED1", newColor);
                    }}
                  />
                </div>
              ))}
            </div>
          </div>

          {/* LED 2 Control */}
          <div className="card mb-3">
            <div className="card-header">
              LED 2
              <button
                className="btn btn-sm btn-primary float-end"
                onClick={() => toggleLed("LED2", led2State, led2Color)}
              >
                {led2State ? "Turn Off" : "Turn On"}
              </button>
            </div>
            <div className="card-body">
              {["Red", "Green", "Blue"].map((color, index) => (
                <div className="mb-3" key={color}>
                  <label>{color}</label>
                  <input
                    type="range"
                    min="0"
                    max="1023"
                    value={led2Color[index]}
                    onChange={(e) => {
                      const newColor = [...led2Color];
                      newColor[index] = parseInt(e.target.value);
                      handleLedChange("LED2", newColor);
                    }}
                  />
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Servo Controls */}
        <div className="col-md-6">
          <h2>Servo Controls</h2>

          {/* Servo 1 Control */}
          <div className="card mb-3">
            <div className="card-header">
              Servo 1
              <button
                className="btn btn-sm btn-primary float-end"
                onClick={() => toggleServo("servo1", servo1State, servo1Angle)}
              >
                {servo1State ? "Stop" : "Start"}
              </button>
            </div>
            <div className="card-body">
              <input
                type="range"
                min="0"
                max="180"
                value={servo1Angle}
                onChange={(e) =>
                  handleServoMove("servo1", parseInt(e.target.value))
                }
              />
              <p>Current Angle: {servo1Angle}°</p>
            </div>
          </div>

          {/* Servo 2 Control */}
          <div className="card mb-3">
            <div className="card-header">
              Servo 2
              <button
                className="btn btn-sm btn-primary float-end"
                onClick={() => toggleServo("servo2", servo2State, servo2Angle)}
              >
                {servo2State ? "Stop" : "Start"}
              </button>
            </div>
            <div className="card-body">
              <input
                type="range"
                min="0"
                max="180"
                value={servo2Angle}
                onChange={(e) =>
                  handleServoMove("servo2", parseInt(e.target.value))
                }
              />
              <p>Current Angle: {servo2Angle}°</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
