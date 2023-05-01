let data = []

for (let i = 1; i < 1000; i++) {
    let n = i;
    let list = [];

    while (n != 1){
        list.push(n);
        console.log(n);
        if (n % 2 == 0){
            n = n / 2;
        }
        else{
            n = n * 3 + 1;
        }
    }
    console.log("1");
    data.push(list)
}

const FileSystem = require("fs");
 FileSystem.writeFile('data.json', JSON.stringify(data), (error) => {
    if (error) throw error;
  });
