const title = document.getElementById("virsraksts")

title.innerHTML = "<i>Čau</i>"
title.style.color = "red"
title.style.backgroundColor = "pink"

const p_element = document.createElement("p")
p_element.innerHTML = "Laura Sprenne"
document.body.append(p_element)

const saraksts = document.createElement("ul")

const elem1 = document.createElement("li")
elem1.innerHTML = "Mārcis"

const elem2 = document.createElement("li")
elem2.innerHTML = "Deivids"

saraksts.append(elem1)
saraksts.append(elem2)

document.body.append(saraksts)

let skaits = 0
const count = document.getElementById("count")
count.innerHTML = 0

function plusOne(){
    skaits += 1
    count.innerHTML = skaits
}

