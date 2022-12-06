// Para copiar `` b n @

// let endpoint = "https://api.binance.com/api/v3/ticker/price"

// const pet = document.querySelector("#button");
//     setInterval(()=>{
//         const list = document.querySelector(".list");
//         axios({
//             method:"GET",
//             url:"https://api.binance.com/api/v3/ticker/price"
//         }).then(res=>{
//             let data = res.data;
//             let text = "";
//             for(let i = 0; i<10; i++){
//                 text += `<li class="id">${data[i].symbol}:</li><li class="price">${data[i].price}uSd$</li>`;
//             }
//             list.innerHTML = text;
//         })
//     },1000);
    
const apiKey = "4d8fb5b93d4af21d66a2948710284366";
const put = document.querySelector(".input");
const send = document.querySelector(".send");
const nameL = document.querySelector(".lugar");
const tempM = document.querySelector(".tempM");
const tempm = document.querySelector(".tempm");
const dataW = document.querySelector(".weather");
const cont = document.querySelector(".container");
send.addEventListener("click",()=>{
    console.log("si");
    axios({
        method:"GET",
        url:`https://api.openweathermap.org/data/2.5/weather?q=${put.value}&appid=${apiKey}&units=metric`
    }).then(res=>{
        put.value = put.value.toUpperCase();
        nameL.innerHTML = put.value;
        put.value="";
        console.log(res);
        const data = res.data;
        let temp = data.main;
        let weather = data.weather;
        tempM.innerHTML = `Max:${temp.temp_max}°C`;
        tempm.innerHTML = `Min:${temp.temp_min}°C`;
        dataW.innerHTML = weather[0].description;
        console.log(weather[0].description)
        cont.style.display="block";    
    })
});


// pet.addEventListener("click",()=>{
//     axios({
//         method:"GET",
//         url: 'https://www.w3.org/TR/2017/REC-WebCryptoAPI-20170126/'
//     }).then(res=>{
//         console.log(res.data);
//     //     const list = document.querySelector("#list");
//     //     const frag = document.createDocumentFragment();
//     //     for(const userI of res.data){
//     //         const listItem = document.createElement("LI");
//     //         listItem.textContent = `${userI.id} - ${userI.name}`
//     //         frag.appendChild(listItem);
//     //     }
//     //     list.appendChild(frag);
//     // }).catch(err=> console.log(err))
//     })
// })