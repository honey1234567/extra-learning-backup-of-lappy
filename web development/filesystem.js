let fs = require("fs");
//read file
let buffer = fs.readFileSync("abc.js");
// console.log("bin data",buffer);//
// console.log("non bin data" + buffer);
// //create file in write mode
 fs.openSync("abc.txt","w");
 fs.writeFileSync("abc.txt","Hum aaj bahut khush hai");//create and replace content in file
//update
fs.appendFileSync("abc.txt","bhai khush kyu nahi hai");

fs.mkdirSync("meridirectory");
fs.writeFileSync("meridirectory/merifile.txt","mera content");//make directory and update content

//to remove files from directory
let content = fs.readdirSync("meridirectory");
console.log(content);
for(let i= 0 ;i<content.length;i++){
    console.log("file",content[i],"is removed");
    fs.unlinkSync("meridirectory/" + content[i]);
}

fs.rmdirSync("meridirectory")//remove folder

//if a file exist at a path then return true else false
let datapathexist = fs.existsSync("abc.txt");
console.log(datapathexist);
let detailsobject = fs.lstatSync(__dirname,"\\filesystem.js");
let ans = detailsobject.isFile();
console.log(ans)
 ans = detailsobject.isDirectory()
console.log(ans);

for(let i=1;i<=10;i++){
    let dirpathtomake = 'lecture-'+i;
    fs.mkdirSync(dirpathtomake);
    fs.writeFileSync(dirpathtomake + "\\" + "readme.md",'# readme for' +dirpathtomake);
}

