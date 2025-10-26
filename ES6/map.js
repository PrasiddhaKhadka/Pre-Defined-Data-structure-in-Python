var numbers = [1, 2, 3, 4, 5];

// The .map() method creates a new array by applying a function to every element of an existing array.

var doubled = numbers.map(function (number){
    return number * 2;
})

console.log(doubled);





// implement the pluck functions
var paints = [ { color: 'red' }, { color: 'blue' }, { color: 'yellow' }];
pluck(paints, 'color'); // returns ['red', 'yellow', 'blue'];

paints.map(function (paint){
    return paint.color
})

