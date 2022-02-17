//db.collections().get() is a asynchronous function and thus returns a promise. Therefore we can use .then and .catch methods on it
// snapshot is basically the state of that collection at that point of time
const list = document.querySelector("ul");
const form = document.querySelector("form");
const button = document.querySelector("button");

// data-id is custom data attribute of HTML
const addRecipe = (recipe, id) => {
  let time = recipe.created_at.toDate();
  let html = `
    <li data-id="${id}">
    <div>${recipe.title}</div>
    <div>${time}</div>
    
    <button class="btn btn-danger btn-sm my-2">Delete</button>
    </li>`;
  list.innerHTML += html;
};

// remove documents in UI
const deleteRecipe = (id) => {
  const recipes = document.querySelectorAll("li");
  recipes.forEach((recipe) => {
    if (recipe.getAttribute("data-id") === id) {
      recipe.remove();
    }
  });
};

// get documents
// db.collection("recipes")
//   .get()
//   .then((snapshot) =>
//     // when we have the data do this
//     {
//       snapshot.docs.forEach((doc) => {
//         addRecipe(doc.data(), doc.id);
//       });
//     }
//   )
//   .catch((err) => console.log(err));

// get documents using REAL TIME LISTENERS
//when state changes in any way, firestore takes a snapshot of that collection
//docChanges method saves any changes that have happened in the collection
// db.collection("recipes") returns a function value, we store its value in a variable. When that function is invoked, real time listening is stopped.

const unsub = db.collection("recipes").onSnapshot((snapshot) => {
  snapshot.docChanges().forEach((change) => {
    const doc = change.doc;
    if (change.type === "added") {
      addRecipe(doc.data(), doc.id);
    } else if (change.type === "removed") {
      deleteRecipe(doc.id);
    }
  });
});

//add documents
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const now = new Date();
  const recipe = {
    title: form.recipe.value,
    //creating a firebase timestamp object
    created_at: firebase.firestore.Timestamp.fromDate(now),
  };

  //we pass in a js object
  // asynchronous function that returns a promise
  db.collection("recipes")
    .add(recipe)
    .then(() => {
      console.log("recipe added");
    })
    .catch((err) => console.log(err));
});

//deleting data
// making use of event delegation
list.addEventListener("click", (e) => {
  if (e.target.tagName === "BUTTON") {
    const id = e.target.parentElement.getAttribute("data-id");
    // this is also async and returns a promise
    db.collection("recipes")
      .doc(id)
      .delete()
      .then(() => console.log("recipe deleted"))
      .catch((err) => console.log(err));
  }
});

//unsub from database changes
button.addEventListener("click", () => {
  unsub();
  console.log("Unsubscribed from UI changes");
});
