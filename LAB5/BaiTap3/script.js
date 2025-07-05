const items = [
  { name: "Book", price: 20000 },
  { name: "Pen", price: 5000 },
  { name: "Bag", price: 100000 },
];

const productList = document.getElementById("productList");
const totalEl = document.getElementById("total");
const clearBtn = document.getElementById("clearBtn");
let total = 0;
let cartItems = [];

// Show product list
items.forEach(item => {
  const li = document.createElement("li");
  const addBtn = document.createElement("button");
  addBtn.textContent = "Add";

  addBtn.onclick = () => {
    cartItems.push(item);
    total += item.price;
    updateTotal();
  };

  li.textContent = `${item.name} - ${item.price} VND `;
  li.appendChild(addBtn);
  productList.appendChild(li);
});

function updateTotal() {
  totalEl.innerText = total;
}

clearBtn.addEventListener("click", () => {
  cartItems = [];
  total = 0;
  updateTotal();
});
