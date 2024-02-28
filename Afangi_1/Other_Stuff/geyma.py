    
    current_button_state = takki_1.value() # Lesa síðasta gildi í breytu
    
    # Check if the button state has changed from low to high
    if current_button_state and not last_button_state:
        led_state = not led_state # Toggla
        if led_state:
            delay_time = random.randint(100, 1000) # Random delay
            sleep_ms(delay_time)
        rautt.value(led_state)
        
    last_button_state = current_button_state # update the last known state
    
    sleep_ms(20)