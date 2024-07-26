
const custom_prefix = '#step';

// this will cut up a single long page into multiple 'subpages' that can be navigated through
// sphinx will give them the hash #{text} where text is the title of the section or #id{number} if the title is a number.
// this script will find the index of that section and convert it to #step{number} and show that section.



window.onload = (event) => {
  // Fix for the scrollbar issue in books theme:
  // https://github.com/executablebooks/sphinx-book-theme/issues/732
  let footer = document.getElementById('rtd-footer-container');
  footer.remove();

  // Fix to add languea selector button to header:
  // https://github.com/executablebooks/sphinx-book-theme/issues/797
//  let header = document.getElementsByClassName('article-header-buttons')[0];
//  header.append("<div>L</div>");
  update_from_hash();
};

function update_from_hash(){
  // Get the id of the active section
  let id = 1;
  if(window.location.hash){
    const hash = window.location.hash;
    if(hash.startsWith(custom_prefix)){
    id = parseInt(window.location.hash.substring(custom_prefix.length)); // remove #step prefix
    } else {
      id = hash.substring(1); // when the hash is not the number.
    }
  }
  show(id);
};
window.onhashchange = function(event)
{
  update_from_hash();
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
  if(typeof id === 'string'){ // when the hash is not the number. This will convert it to the num of the section.
    for (i = 1; i < sections.length; ++i){
      if(sections[i].id === id){
        id = i;
        break;
      }
    }
  }
  sections[id].style.display = 'block';
  showFooter(id, sections);
  window.location.hash = custom_prefix + id;
}

