document.addEventListener('DOMContentLoaded', function () {
    const resultInput = document.getElementById('result');
    const buttons = document.querySelectorAll('button');

    let currentInput = '';
    let currentOperator = '';
    let calculationDone = false;

    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            const buttonText = button.textContent;

            if (buttonText >= '0' && buttonText <= '9') {
                if (calculationDone) {
                    currentInput = '';
                    calculationDone = false;
                }
                currentInput += buttonText;
            } else if ('+-*/'.includes(buttonText)) {
                if (currentInput !== '') {
                    if (currentOperator !== '') {
                        calculate();
                    }
                    currentOperator = buttonText;
                    currentInput += buttonText;
                }
            } else if (buttonText === '=') {
                calculate();
                calculationDone = true;
            } else if (buttonText === 'C') {
                clear();
            } else if (buttonText === '←') {
                backspace();
            } else if (buttonText === '.') {
                if (!currentInput.includes('.')) {
                    currentInput += '.';
                }
            }

            resultInput.value = currentInput;
        });
    });

    function calculate() {
        try {
            currentInput = eval(currentInput).toString();
        } catch (error) {
            currentInput = 'Error';
        }
        currentOperator = '';
    }

    function clear() {
        currentInput = '';
        currentOperator = '';
        calculationDone = false;
    }

    function backspace() {
        currentInput = currentInput.slice(0, -1);
    }
});
