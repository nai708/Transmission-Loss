
def current_amps(power, voltage):
    current = power / voltage
    return current

def p_loss(current, resistance):
    power_loss = (current**2) * resistance
    return power_loss

def t_resistance(resistance_perkm, length_km):
    # Total resistance is used to calculate total power wasted by entire system.
    total_resistance = resistance_perkm * length_km
    # A version of series addition, since resistance_perkm is a rate (it assumes the pieces are identical).
    return total_resistance