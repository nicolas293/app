
function onClickMenu() {
    var menuClick = document.getElementById('menuClick');
    var wrapper = document.getElementById('wrapper');
    var menuClick = document.getElementById('menuClick');
    var WrapperMainStuctures = document.getElementById('WrapperMainStuctures');
    var clonMainWrapper = document.getElementById('clonMainWrapper');

        if (wrapper.style.display == "block") {
            wrapper.style = "none";
            clonMainWrapper.style = "none";
            menuClick.innerHTML = "Скрыть Сайт";
            clonMainWrapper.style = "block";
            wrapper.style.display = "block";
        } else {       
            wrapper.style.display = "block";
            clonMainWrapper.style = "none";
            menuClick.innerHTML = "Открыть Сайт";
            clonMainWrapper.style = "block";
            wrapper.style = "none";    
        }

        if (WrapperMainStuctures.style.display == "block") {
            WrapperMainStuctures.style.display = "block";
            clonMainWrapper.style = "block";
            menuClick.innerHTML = "Скрыть Сайт";
            clonMainWrapper.style = "none";
            WrapperMainStuctures.style = "none";
        } else {
            WrapperMainStuctures.style = "none";
            clonMainWrapper.style = "none";
            menuClick.innerHTML = "Открыть Сайт";
            clonMainWrapper.style = "block";
            WrapperMainStuctures.style.display = "block";   
        }    
    }
