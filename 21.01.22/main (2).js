// 1. ievērojot pareizu tabulas HTML struktūru, aizpildīt tabulu ar vienu rindu, kas satur
// 3 šūnas - vārdu, uzvārdu, klasi

const table = document.getElementById("name")

const tr = document.createElement("tr")
const elem1 = document.createElement("td")
elem1.innerHTML = "Laura"

const elem2 = document.createElement("td")
elem2.innerHTML = "Sprenne"

const elem3 = document.createElement("td")
elem3.innerHTML = "11c"

table.append(elem1)
table.append(elem2)
table.append(elem3)

// 2. klikšķinot abas pogas, attiecīgā count elementa saturam jāpalielinās par 1

let skaits1 = 0
const count1 = document.getElementById("count1")
count1.innerHTML = skaits1

function plusOne1() {
    skaits1 += 1
    count1.innerHTML = skaits1
    let sum = document.getElementById("sum")
    summa = skaits1 + skaits2
    sum.innerHTML = summa
}

let skaits2 = 0
const count2 = document.getElementById("count2")
count2.innerHTML = skaits2

function plusOne2() {
    skaits2 += 1
    count2.innerHTML = skaits2
    let sum = document.getElementById("sum")
    summa = skaits1 + skaits2
    sum.innerHTML = summa
}

// 3. summas elementā uzrādīt abu count elementu summu
let sum = document.getElementById("sum")
summa = skaits1 + skaits2
sum.innerHTML = summa

// 4. switch theme nomaina lapas motīvu, ja fons ir balts un teksts melns -
// nomaina fonu un melnu un tekstu uz baltu un otrādi.
document.body.style.backgroundColor = "white"

function switchTheme() {
    if (document.body.style.backgroundColor === "white"){
        document.body.style.backgroundColor = "black";
        document.body.style.color = "white";
    } else{
        document.body.style.backgroundColor = "white";
        document.body.style.color = "black";
    }
}
 