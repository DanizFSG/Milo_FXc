const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    toggle = body.querySelector(".toggle"),
    searchBtn = body.querySelector(".search-box"),
    modeSwtich = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".moden-text");

    toggle.addEventListener("click",() =>{
        sidebar.classList.toggle("close");
    })


    modeSwtich.addEventListener("click",() =>{
        body.classList.toggle("dark");

        if(body.classList.contains("dark")){
            modeText.textContent = "Light Mode";
        }else{
            modeText.textContent = "Dark Mode";
        }
    })