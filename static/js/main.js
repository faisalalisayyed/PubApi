var page = 1;

get_data(page);

function pre() {
  if (page > 1) {
    page = page - 1;
    get_data(page);
  }
}

function next() {
  if (page >= 1) {
    page = page + 1;
    get_data(page);
  }
}

function get_data(page) {
  var button = document.getElementById("pagination");
  button.style.display = "block";
  $.ajax({
    url: "/get_data",
    data: { page: page },
    type: "GET",
    success: function (response) {
      const data = response.data;
      const content = $("#data-from-js");
      content.empty();
      for (let i = 0; i < data.length; i++) {
        content.append(`
        <div class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
            <div class="flex flex-col">
                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${data[i]["API"]}</h5>
                <p class="font-normal text-gray-700 dark:text-gray-400">${data[i]["Category"]}</p>
                <a href="${data[i][" Link"]}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">API Docs Link</a>
            </div>
            <hr class="border-gray-300 my-4">
  
            <div class="mt-4 grid grid-cols-3 gap-4">
                <div>
                    <p class="text-sm font-semibold">Auth</p>
                    <div class="flex items-center space-x-2">
                        <p class="text-gray-600">${data[i]["Auth"]}</p>
                    </div>
                </div>
                <div>
                    <p class="text-sm font-semibold">HTTPS</p>
                    <div class="flex items-center space-x-2">
                        <p class="text-gray-600">${data[i]["HTTPS"]}</p>
                    </div>
                </div>
                <div>
                    <p class="text-sm font-semibold">Cors</p>
                    <div class="flex items-center space-x-2">
                        <p class="text-gray-600">${data[i]["Cors"]}</p>
                    </div>
                </div>
                <div class="col-span-3">
                    <h4 class="text-lg font-semibold">Description</h4>
                    <p class="text-gray-600">${data[i]["Description"]}</p>
                </div>
            </div>
        </div>
        `);
      }
    },
    error: function (error) {
      console.log(error);
    },
  });
}

document.getElementById("mySelect").addEventListener("change", function () {
  var selectedValue = this.value;
  if (selectedValue === "all") {
    console.log("working");
    get_data(1);
  } else {
    var button = document.getElementById("pagination");
    button.style.display = "none";
    $.ajax({
      url: "/filter",
      data: { cate: selectedValue },
      type: "GET",
      success: function (response) {
        const data = response.data;
        const content = $("#data-from-js");
        content.empty();
        for (let i = 0; i < data.length; i++) {
          content.append(`
            <div class="block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
                <div class="flex flex-col">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${data[i]["API"]}</h5>
                    <p class="font-normal text-gray-700 dark:text-gray-400">${data[i]["Category"]}</p>
                    <a href="${data[i][" Link"]}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">API Docs Link</a>
                </div>
                <hr class="border-gray-300 my-4">
      
                <div class="mt-4 grid grid-cols-3 gap-4">
                    <div>
                        <p class="text-sm font-semibold">Auth</p>
                        <div class="flex items-center space-x-2">
                            <p class="text-gray-600">${data[i]["Auth"]}</p>
                        </div>
                    </div>
                    <div>
                        <p class="text-sm font-semibold">HTTPS</p>
                        <div class="flex items-center space-x-2">
                            <p class="text-gray-600">${data[i]["HTTPS"]}</p>
                        </div>
                    </div>
                    <div>
                        <p class="text-sm font-semibold">Cors</p>
                        <div class="flex items-center space-x-2">
                            <p class="text-gray-600">${data[i]["Cors"]}</p>
                        </div>
                    </div>
                    <div class="col-span-3">
                        <h4 class="text-lg font-semibold">Description</h4>
                        <p class="text-gray-600">${data[i]["Description"]}</p>
                    </div>
                </div>
            </div>
        `);
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  }
});
