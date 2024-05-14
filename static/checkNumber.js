const answerEl = document.querySelector('#answer')
const checkBtn = document.querySelector('#check')
const resultEl = document.querySelector('#result')
const doneEl = document.querySelector('#done')
const resultsBtn = document.querySelector('#results')


const showResult = (result) => {
	resultEl.textContent = result ? 'умница молодец' : 'думай еще'
}

const showDone = () => {
	doneEl.textContent = 'Попытки закончились!!!!'
}

const deactivate = () => {
	answerEl.disabled = true
	checkBtn.disabled = true
}

const showResultsBtn = () => {
	resultsBtn.style.display = 'block'
}

const handleDone = (name) => {
	showDone()
	deactivate()
	showResultsBtn()

	resultsBtn.addEventListener('click', () => {
		window.location = `http://localhost/results?name=${name}`
	})
}


checkBtn.addEventListener('click', async e => {
	e.preventDefault()
	const url = window.location.search;
	const urlParams = new URLSearchParams(url);
	const name = urlParams.get('name')

	const answer = answerEl.value

	const result = await get(`http://localhost/api/check_answer?name=${name}&answer=${answer}`)
	const done = await get(`http://localhost/api/done?name=${name}`)

	showResult(result)

	if (done) {
		handleDone(name)
	}
})

