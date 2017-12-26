"use strict";

/*
Задача: написать функцию, которая принимает произвольный массив целых чисел
и возвращает минимальное, положительное число, которое отсутствует в 
данном массиве, так например: [1, 3, 6, 4, 1, 2] должна быть возвращена 5

выделенное время: 30 мин.

затраченное время: 1 час 20 мин.
*/


var a = [1, 3, 6, 4, 1, 2]; // must return 5
var b = [1, 2, 15];
var d = [-1, -2, -15];
var e = [-1, -2, -15, 1, 2, 120];
var ArraNull = [-1, -2, 0,0,0,0,1,2,123]; 

function answer(array) {
    // служебная функция для метода sort, особенность языка JS
    function compareNumeric(a, b) {
        if (a > b) return 1;
        if (a < b) return -1;
    }
    // функция возвращает массив только позитивных чисел исходного массива 
    function positiveNumbers(array) {
        var newArra = [];
        for (var i = 0; i < array.length; i++ ) {
            if (array[i] > 0) {
                newArra.push(array[i]);
            }
        }
        return newArra;
    }
    // algorithm: step 1
    var c = array.sort(compareNumeric);
    // algorithm: step 2
    var newC = positiveNumbers(c);  
    if (newC.length < 1) {
        return 1;
    }
    // algorithm: step 3
    var index = 1;
    var answ;
    for (var i = 0; i < newC.length; i++) {
        newC.indexOf(index) >= 0 ? index++ : answ = index;
    }
    return answ;
}

console.log(a);
var answers = answer(a);
console.log(answers);
