// Encapsulation in JavaScript
// 
// Whether it is Python or JavaScript(this example), Object-Oriented Programming works by grouping related variables and functions that operate on them into Objects; <- This is called "Encapsulation":

// This is an example of a procedural approach to a problem in JavaScript;
// Below I have 3 variables, and below those I have a function to calculate the wage of an employee.
// This is Procedural because I have variables on one side, and functions on the other side.

let baseSalary = 80_000;
let overtime = 20;
let rate = 40;

function getWage(baseSalary, overtime, rate) {
  console.log(baseSalary + (overtime * rate))
  return baseSalary + (overtime * rate)
}

getWage(baseSalary, overtime, rate);



// Below is an example of an Object-Oriented way to solve the same problem.
// Instead of having the 3 variables and then the function, I can have an 'employee' object with 3 properties and the method 'getWage':

let employee = {
  baseSalary: 80_000,
  overtime: 20,
  rate: 40,
  getWage: function() { 
    console.log(baseSalary + (overtime * rate))
    return this.baseSalary + (this.overtime * this.rate);
  }
};

employee.getWage();

// This is better because the 'getWage' function has no parameters. In the procedural example the same fucntion had 3 parameters; In the OOP example all 3 of the original parameters are not modeled as properties of the 1 employee object; All the properties, and the getWage function are related, so they are a part of one unit.
//  When you write in an OOP way, your functions have fewer parameters, which is ideal because this is easier to use and maintain.