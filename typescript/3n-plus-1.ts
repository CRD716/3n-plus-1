let data:number[] = []
import { writeFile } from 'fs/promises';

for (let i = 1; i < 1000; i++) {
    let n:number = i;
    let list:number[] = [];

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
    data.push(list);
}

writeFile('data.json', JSON.stringify(data));
