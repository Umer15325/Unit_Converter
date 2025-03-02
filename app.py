import streamlit as st


def convert_length(value, from_unit, to_unit):
    length_conversions = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        'grams': 1.0,
        'kilograms': 1000.0,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value
    




def main():
    st.title("Unit Converter")

    conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

    if conversion_type == "Length":
        units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'inches', 'feet', 'yards', 'miles']
    elif conversion_type == "Weight":
        units = ['grams', 'kilograms', 'milligrams', 'pounds', 'ounces']
    elif conversion_type == "Temperature":
        units = ['celsius', 'fahrenheit', 'kelvin']

    # Input value
    value = st.number_input("Enter the value to convert", value=1.0)

    # Select the 'from' unit
    from_unit = st.selectbox("From", units)

    # Select the 'to' unit
    to_unit = st.selectbox("To", units)

    # Perform the conversion
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    # Display the result
    st.write(f"Converted value: {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()