var colors = ['red', 'blue', 'green', 'yellow'];


// Traditional for loop
for (var i = 0; i < colors.length; i++){
    console.log(colors[i]);
}

// ES6 for...of loop
colors.forEach(function (color){
    console.log(color);
})


// adding the number of a list using array methods

var numbers = [1, 2, 3, 4, 5];

var sum = 0 ;

// or cloud have made a function and pass the function 

// function adder(number){
//     sum += number;
// }

numbers.forEach(function (number){
    // and pass the refrence here 
    sum += number;
})

console.log('Your total is: ' + sum);




// lest filter using for each for a dictinary in ES6 javascript

var products = [
    {name: 'cucumber', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'apple', type: 'fruit'}
];

var fruits = [];
products.forEach(function (product){
    if (product.type === 'fruit'){
        fruits.push(product);
    }
}
)
console.log(fruits);


