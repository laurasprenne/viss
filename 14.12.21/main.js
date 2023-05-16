function setValue(){
    const element = document.getElementById("input").value;
    const field = document.getElementById("field");
    field.innerHTML = "";

    const known = [value[0]];

    for(let i = 0; i < value.length; i++){
        for(const c of known){
            if(c === value[i]){
                field.innerHTML += c;
            }
            else{
                field.innerHTML += "_";
            }
        }
    }
}
