
function setCalendarMonth(oldDate) {
	const monthHeader = document.querySelector("#month-header")
	const calendarBody = document.querySelector("#calendar-days");

	const date = new Date(oldDate);
	date.setDate(1);

	const monthNames = [
		"January", "February", "March", "April", "May", "June", 
		"July", "August", "September", "October", "November", "December"
	];

	const currentMonth = date.getMonth();

	monthHeader.innerText = `${monthNames[currentMonth]} ${date.getFullYear()}`;

	// Move the date back to the first day that will show up on the calendar.
	date.setDate(1 - date.getDay())

	for(let i = 0; i < calendarBody.children.length; i++) {
		const row = calendarBody.children[i];
		
		for(let j = 0; j < row.children.length; j++) {
			const cell = row.children[j];

			cell.innerText = date.getDate();
			cell.classList.toggle("outside-of-month", date.getMonth() !== currentMonth);
			cell.classList.toggle("after-month", date.getMonth() === ((currentMonth + 1) % 12));

			cell.setAttribute("data-date", date.getTime());

			date.setDate(date.getDate() + 1);
		}
	}
}


window.addEventListener("load", () => {
	const calendarBody = document.querySelector("#calendar-days");

	let startDate = null;

	function onDayClick(e) {
		const dayElement = e.target;

		if(startDate === null) {
			startDate = new Date(+dayElement.getAttribute("data-date"));
			document.querySelec
		}
	}


	for(let i = 0; i < 6; i++) {
		const row = document.createElement("tr");
		for(let j = 0; j < 7; j++) {
			const day = document.createElement("td");

			day.classList.add("calendar-cell");
			row.appendChild(day);

			day.addEventListener("click", () => {

			});
		}
		calendarBody.appendChild(row);
	}

	const calendarDate = new Date();



	setCalendarMonth(calendarDate);

	document.querySelector("#prev-month-button").addEventListener("click", () => {
		calendarDate.setMonth(calendarDate.getMonth() - 1);
		setCalendarMonth(calendarDate);
	});
	document.querySelector("#next-month-button").addEventListener("click", () => {
		calendarDate.setMonth(calendarDate.getMonth() + 1);
		setCalendarMonth(calendarDate);
	});
});