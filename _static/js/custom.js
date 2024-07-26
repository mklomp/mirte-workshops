window.onload = (event) => {
  // Fix for the scrollbar issue in books theme:
  // https://github.com/executablebooks/sphinx-book-theme/issues/732
  let footer = document.getElementById('rtd-footer-container');
  footer.remove();

  // Fix to add languea selector button to header:
  // https://github.com/executablebooks/sphinx-book-theme/issues/797
//  let header = document.getElementsByClassName('article-header-buttons')[0];
//  header.append("<div>L</div>");

  // Get all sections in the page
  let sections = document.getElementsByTagName('section');

  // Get the id of the active section
  let id = 1;
  let split_url = window.location.href.split("#")
  if (split_url[1]){
    id = split_url[1].substr(2);
  }

  showFooter(id, sections);
};


function showFooter(current, sections){
  // Enable empty footer
  let area = document.getElementsByClassName('prev-next-area')[0];
//  let footer = document.getElementsByClassName('prev-next-footer')[0];
  area.innerHTML = "";
//  footer.style.display = 'block';

  // And possibly fill it
  if (current != 1){
    area.innerHTML += '<a class="left-prev" href="javascript:show(' + (current - 1) + ')" title="previous step"> \
      <i class="fa-solid fa-angle-left"></i> \
      <div class="prev-next-info"> \
        <p class="prev-next-subtitle">previous</p> \
      </div> \
    </a>';
  }
  if (sections.length != 1 && current != sections.length - 1){
   area.innerHTML += '<a class="right-next" href="javascript:show(' + (current + 1) + ')" title="next step"> \
      <div class="prev-next-info"> \
        <p class="prev-next-subtitle">next</p> \
      </div> \
      <i class="fa-solid fa-angle-right"></i> \
    </a>';
  }
}


function show(id){
  let sections = document.getElementsByTagName('section');

  for (i = 1; i < sections.length; ++i){
    sections[i].style.display = 'none';
  }
  sections[id].style.display = 'block';
  showFooter(id, sections);

}

