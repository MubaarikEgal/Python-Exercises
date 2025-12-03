"use strict";

const form = document.getElementById("search-form");
const queryInput = document.getElementById("query");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const searchTerm = queryInput.value.trim();
    if (!searchTerm) return;


    resultsDiv.innerHTML = "";


    const url = `https://api.tvmaze.com/search/shows?q=${searchTerm}`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);


    data.forEach(tvShow => {
        const show = tvShow.show;


        const article = document.createElement("article");


        const h2 = document.createElement("h2");
        h2.textContent = show.name || "No name available";
        article.appendChild(h2);


        if (show.url) {
            const link = document.createElement("a");
            link.href = show.url;
            link.target = "_blank";
            link.textContent = "More details";
            article.appendChild(link);
        }


        const img = document.createElement("img");
        img.src = show.image?.medium || "";
        img.alt = show.name || "Show image";
        article.appendChild(img);


        const summaryDiv = document.createElement("div");
        summaryDiv.innerHTML = show.summary || "No summary available.";
        article.appendChild(summaryDiv);


        resultsDiv.appendChild(article);
    });
});
