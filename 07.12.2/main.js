let x;
x = 8;
const y = 23;

// for(let i = 0; i < 5; i++){
//     console.log(i)
// }
// if(x > 5){
//     console.log("ok")
// }
// else{
//     console.log("no")
// }
// while(x > 0){
//     console.log(x)
//     x--:
// }
// const a = [1, 4, 2, 7, 2]
// console.log(a[7])

// for(const item of a){
//     console.log(item)
// }

// let obj = {
//     name: "Laura",
//     age: 17
// }
// console.log(obj.age)

// function funkcijas_nosaukums(a, b){
//     return a + b
// }
// console.log(funkcijas_nosaukums(2, 3))

const page = document.createElement("p")
page.innerHTML = "<h1>Hey</h1>"
page.classList.add("red")
document.body.appendChild(page)
const list = document.createElement("ul")
boys = ["Mārcis", "Toms", "Tomass"]

for(const boy of boys){
    list.innerHTML += "<li>" + boy + "</li>"
}

document.body.appendChild(list)

const people = [
    {
        name:"Laura",
        surname:"Sprenne",
        age: 17
    },
    {
        name:"Elīna",
        surname:"Zēniņa",
        age: 12
    },
    {
        name:"Jānis",
        surname:"Paraudziņš",
        age: 4
    }
]

const table = document.createElement("table");

for(const person of people){
    const row = document.createElement("tr");
    for(const attribute in person){
        row.innerHTML += "<td>" + person.attribute + "</td>";
    }
    table.appendChild(row);
}

table.style.border ="1px solid black"

document.body.appendChild(table)
