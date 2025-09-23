function sayGoodBye(){
    console.log("goodbye");
}

function sayHello(){
    const timeout = setTimeout(()=>{console.log("Hello")}, 1000);   
    sayGoodBye();
    
    }


    sayHello();
