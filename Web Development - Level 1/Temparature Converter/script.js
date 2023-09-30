document.addEventListener('DOMContentLoaded', function () {
    const temperatureInput = document.getElementById('temperature');
    const unitSelect = document.getElementById('unit');
    const convertButton = document.getElementById('convert');
    const resultDiv = document.getElementById('result');

    convertButton.addEventListener('click', function () {
        const temperature = parseFloat(temperatureInput.value);
        const unit = unitSelect.value;
        let convertedTemperature = 0;
        let resultText = '';

        if (isNaN(temperature)) {
            resultText = 'Please enter a valid number.';
        } else {
            if (unit === 'celsius') {
                convertedTemperature = (temperature - 32) * (5 / 9) + 273.15;
                resultText = `Converted Temperature: ${convertedTemperature.toFixed(2)} K`;
            } else if (unit === 'fahrenheit') {
                convertedTemperature = (temperature + 459.67) * (5 / 9);
                resultText = `Converted Temperature: ${convertedTemperature.toFixed(2)} K`;
            } else if (unit === 'kelvin') {
                convertedTemperature = temperature;
                resultText = `Converted Temperature: ${convertedTemperature.toFixed(2)} K`;
            }
        }

        resultDiv.textContent = resultText;
    });
});
