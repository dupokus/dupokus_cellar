function fizzBuzz(n) {
    answer = []

    for (var i = 0; i < n; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            answer.push("Fizzbuzz");
        } else if (i % 3 === 0 && i % 5 != 0) {
            answer.push("Fizz");
        } else if (i % 5 === 0 && i % 3 != 0) {
            answer.push("Buzz");
        } else {
            answer.push(`${i+1}`);
        }
    }
    return answer;
}
let i = Math.floor(Math.random() * 10);
console.log(i);
console.log(fizzBuzz(16));

