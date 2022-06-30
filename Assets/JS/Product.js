var sum;
var length;
var prices = document.querySelectorAll(".price");
var totalPrice = document.getElementById("totalPrice");
var basketedBooks = document.getElementById("basketedBooks");
var priceOfBook = document.getElementById("priceOfBook");
var price = parseInt(priceOfBook.innerHTML);
function SumAndLength() {
  sum = 0;
  length = 0;
  prices = document.querySelectorAll(".price");
  prices.forEach(element => {
    sum += parseInt(element.innerHTML);
    length = prices.length;
  });
  totalPrice.innerHTML = sum;
  basketedBooks.innerHTML = length;
}
SumAndLength();
const like = document.getElementById("like");
like.addEventListener("click", function (event) {
  if (event.target.className == "bi bi-hand-thumbs-down-fill text-secondary") {
    event.target.className = "bi bi-hand-thumbs-up-fill text-primary";
  }
  else {
    event.target.className = "bi bi-hand-thumbs-down-fill text-secondary";
  }
});
const heart = document.getElementById("heart");
heart.addEventListener("click", function (event) {
  if (event.target.className == "bi bi-heart-fill text-secondary") {
    event.target.className = "bi bi-heart-fill text-danger";
    alert("Kitabı bəyəndiniz!");
  }
  else {
    event.target.className = "bi bi-heart-fill text-secondary";
    alert("Bəyənməkdən imtina etdiniz!");
  }
});
var removeSign = document.querySelectorAll(".removeItem");
removeSign.forEach(element => {
  element.addEventListener("click", function (event) {
    var removedList = element.closest("li");
    removedList.remove();
    SumAndLength();
    if (length == 0) {
      basketedBooks.classList.add("d-none");
    }
  })
});
const basket = document.getElementById("basket");
var alertModal = document.querySelector(".modal-body");
basket.addEventListener("click", function(event) {
  const infoAlert = document.getElementById("infoAlert");
  if (basket.className == "btn text-light bg-info") {
    basket.className = "btn text-light bg-secondary";
    basket.innerHTML = "Səbətdən çıxart";
    infoAlert.className = "alert alert-danger mt-2 text-center";
    infoAlert.innerHTML = "Bu kitabdan sadəcə <b>1</b> ədəd qalıb";
    var list = document.getElementById("myList");
    var listItem = document.createElement("li");
    list.insertBefore(listItem, list.children[0]);
    var mainDiv = document.createElement("div");
    listItem.appendChild(mainDiv);
    mainDiv.classList.add("dropdown-item", "px-3", "d-flex", "justify-content-between", "py-0");
    var div_d_flex = document.createElement("div");
    div_d_flex.classList.add("d-flex")
    mainDiv.appendChild(div_d_flex);
    var div1 = document.createElement("div");
    var span = document.createElement("span");
    span.classList.add("btn", "btn-white", "text-danger", "fs-5", "fw-bolder", "removeItem");
    var signX = document.createTextNode("X");
    span.appendChild(signX);
    div1.appendChild(span);
    var div2 = document.createElement("div");
    div2.classList.add("align-self-center");
    var bookName = document.createTextNode("Inkognito");
    div2.appendChild(bookName);
    div_d_flex.appendChild(div1);
    div_d_flex.appendChild(div2);
    var div_price = document.createElement("div");
    div_price.classList.add("align-self-center");
    mainDiv.appendChild(div_price);
    var span_price = document.createElement("span");
    span_price.classList.add("price");
    var price_of_book = document.createTextNode(price);
    span_price.appendChild(price_of_book);
    var azn = document.createTextNode("AZN");
    div_price.appendChild(span_price);
    div_price.appendChild(azn);
    removeSign = document.querySelectorAll(".removeItem");
    removeSign[0].addEventListener("click", function (event) {
      removedList = removeSign[0].closest("li");
      removedList.remove();
      basket.className = "btn text-light bg-info";
      basket.innerHTML = "Səbətə əlavə et";
      infoAlert.className = "alert alert-warning mt-2 text-center";
      infoAlert.innerHTML = "Bu kitabdan sadəcə <b>2</b> ədəd qalıb";
      SumAndLength();
      if (length == 0) {
        basketedBooks.classList.add("d-none");
      }
    })
    SumAndLength();
    basketedBooks.classList.remove("d-none")
  } else {
    basket.className = "btn text-light bg-info";
    basket.innerHTML = "Səbətə əlavə et";
    infoAlert.className = "alert alert-warning mt-2 text-center";
    infoAlert.innerHTML = "Bu kitabdan sadəcə <b>2</b> ədəd qalıb";
    alertModal.innerHTML = "Məhsul səbətdən çıxarıldı";
    var removeFirstChild = document.getElementById("myList");
    removeFirstChild.removeChild(removeFirstChild.firstElementChild);
    SumAndLength();
    if (length == 0) {
      basketedBooks.classList.add("d-none");
    }
  }
});
