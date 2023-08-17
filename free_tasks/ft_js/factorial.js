function factorial(num) {
    if (typeof num === 'number' && num > 0 && Number.isInteger(num)) {
        let result = 1;
        while (num > 1) {
            result *= num;
            num--;
        }
        console.log(result);
    } else if (num === 0) {
        console.log(1);
    } else {
        console.log("None");
    }
}

factorial(5);
factorial(6);
factorial(0);
factorial(-2);
factorial(1.2);
factorial('Spam spam spam spam spam');
