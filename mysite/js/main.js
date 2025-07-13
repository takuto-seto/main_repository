const typingText = document.querySelector('.MainVisual');
const text = "My Portfolio Site";
let index = 1;

setTimeout(typeText, 1000);
function typeText() {
    typingText.textContent = text.slice(0, index);
    if (index < text.length) {
      index++;
      const randomInterval = Math.floor(Math.random() * 350) + 50;
      setTimeout(typeText, randomInterval);
    } 
  };
  


  window.addEventListener('scroll', function(){
    // スクロール量を取得
    const scroll = window.scrollY;
    // 画面の高さを取得
    const windowHeight = window.innerHeight;
    // すべての.boxを取得
    const boxes = document.querySelectorAll('.box');
  
    boxes.forEach(function(box) {
      // boxまでの高さを取得
      const distanceToBox = box.offsetTop;
      // 下記条件が成り立つときだけboxにis-activeクラスを付与する
      if(scroll + windowHeight > distanceToBox) {
        box.classList.add('is-active');
      }
    });
  }); 
