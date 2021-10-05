// Object Literal N E W
// let character = {
//   name: "Yunjin",
//   stamina: 50,
//   eat: function (portion) {
//     this.stamina = this.stamina + portion;
//     console.log(`Hello ${this.name}, enjoy your food`);
//   },
// }; not effective for more object

// Function Declaration N E W
// function Character(name, energy) {
//   let Character = [];
//   Character.name = name;
//   Character.energy = energy;

//   Character.eat = function (portion) {
//     this.energy += portion;
//     console.log(`Hello ${this.name}. enjoy your food`);
//   };
//   Character.main = function (hours) {
//     this.energy -= hours;
//     console.log(`Hello ${this.name}, Have a nice play`);
//   };

//   return Character;
// }

// let panji = Character("Panji", 89);
// let wendy = Character("Wendy", 50);

// Constructor N E W
// function Character(name, energy) {
//   this.name = name;
//   this.energy = energy;

//   this.eat = function (portion) {
//     this.energy += portion;
//     console.log(`Hello ${this.name}. enjoy your food`);
//   };
//   Character.main = function (hours) {
//     this.energy -= hours;
//     console.log(`Hello ${this.name}, Have a nice play`);
//   };
// }

// let panji = new Character("Panji", 89);
// let wendy = new Character("Wendy", 50);

// Object.create()
// function Character(name, energy) {
//   let Character = {};
//   Character.name = name;
//   Character.energy = energy;
// }
// const methodCharacter = {
//   eat: function (portion) {
//     this.energy += portion;
//     console.log(`Hello ${this.name}, enjoy your food`);
//   },

//   playing: function (hours) {
//     this.energy -= hours;
//     console.log(`Hello ${this.name}, have a nice game!`);
//   },

//   sleep: function (hours) {
//     this.energy += hours * 2;
//     console.log(`Hello ${this.name}, have a good sleep`);
//   },
// };
// function Character(name, energy) {
//   let Character = Object.create(methodCharacter);
//   Character.name = name;
//   Character.energy = energy;

//   return Character;
// }

// let panji = Character("Panji", 121);
// let faris = Character("Faris", 90);

// prototyple inheritance
// function Character(name, energy) {
//   this.name = name;
//   this.energy = energy;
// }
// Character.prototype.eat = function (portion) {
//   this.energy += portion;
//   return `Hello ${this.name}, enjoy your food`;
// };
// Character.prototype.play = function (hours) {
//   this.energy -= hours;
//   return `Hello ${this.name}, enjoy your game`;
// };
// Character.prototype.sleep = function (hours) {
//   this.energy += hours * 2;
//   return `Hello ${this.name}, enjoy your sleep`;
// };

// let panji = new Character("Panji", 12);

// versi class
class Character {
  constructor(name, energy) {
    this.name = name;
    this.energy = energy;
  }
  eat = function (portion) {
    this.energy += portion;
    return `Hello ${this.name}, enjoy your food`;
  };
  play = function (hours) {
    this.energy -= hours;
    return `Hello ${this.name}, enjoy your game`;
  };
  sleep = function (hours) {
    this.energy += hours * 2;
    return `Hello ${this.name}, enjoy your sleep`;
  };
}

let panji = new Character("Panji", 15);
