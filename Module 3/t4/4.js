'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

// Task 4

const target = document.getElementById('target');

for (let i = 0; i < students.length; i++) {
  const opt = document.createElement('option');
  opt.value = students[i].id;
  opt.textContent = students[i].name;
  target.appendChild(opt);
}
