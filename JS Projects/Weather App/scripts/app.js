// DOM manipulation

const cityForm = document.querySelector("form");
const card = document.querySelector(".card");
const details = document.querySelector(".details");
const time = document.querySelector("img.time");
const icon = document.querySelector(".icon img");

const updateCity = async (city) => {
  // we use await here because getCity is an asunchronous function and so it returns a promise. So we wait till it resolves and then assign its value.

  //cityDets now contains the city info. To access the key we use the Key property
  const cityDets = await getCity(city);
  const weather = await getWeather(cityDets.Key);

  //   return {
  //     cityDets: cityDets,
  //     weather: weather,
  //   };

  // Object Shorthand Notation
  //When the obejct property name and value name is same, we can write like this
  return {
    cityDets,
    weather,
  };
};

cityForm.addEventListener("submit", (e) => {
  // prevent default action
  e.preventDefault();

  // get city value
  // trim removes the empty spaces at the end, if any
  const city = cityForm.city.value.trim();
  cityForm.reset();

  // update the ui with new city

  //updateCity recieves a promise
  updateCity(city)
    .then((data) => {
      updateUI(data);
    })
    .catch((err) => {
      console.log(err);
    });
});

const updateUI = (data) => {
  const cityDets = data.cityDets;
  const weather = data.weather;

  // update deatils template
  details.innerHTML = `<h5 class="my-3">${cityDets.EnglishName}</h5>
          <div class="my-3">${weather.WeatherText}</div>
          <div class="display-4 my-4">
            <span>${weather.Temperature.Metric.Value}</span>
            <span>&deg;C</span>
          </div>`;

  // remove the d-none class if present
  if (card.classList.contains("d-none")) {
    card.classList.remove("d-none");
  }

  // update the night/day & icon images

  const iconSrc = `img/icons/${weather.WeatherIcon}.svg`;
  icon.setAttribute("src", iconSrc);

  let timeSrc = null;
  if (weather.IsDayTime) {
    timeSrc = "img/day.svg";
  } else timeSrc = "img/night.svg";

  time.setAttribute("src", timeSrc);
};
