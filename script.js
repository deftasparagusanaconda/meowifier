let meows = [...defaultMeows];
let charToMeow;
let meowToChar;

const text = document.getElementById('text');
const meowsBox = document.getElementById('meows');
const codebook = document.getElementById('codebook');

function rebuildMaps() {
	charToMeow = Object.fromEntries(
		chars.split('').map((char, i) => [char, meows[i]])
	);

	meowToChar = Object.fromEntries(
		meows.map((meow, i) => [
			meow.replaceAll('*', ''),
			chars[i]
		])
	);
}

function charsToMeows(text) {
	return [...text]
		.map(char => charToMeow[char] ?? char)
		.join(' ');
}

function meowsToChars(text) {
	text = text.replaceAll('*', '');
	text += ' ';

	let output = '';
	let buffer = '';

	const it = [...text];

	for (let i = 0; i < it.length; i++) {
		buffer += it[i];

		if (buffer in meowToChar) {
			output += meowToChar[buffer];
			buffer = '';
			i++;
		}
	}

	if (buffer !== '')
		throw new Error(`Could not decode "${buffer}"`);

	return output;
}

function applyCodebook() {
	meows = codebook.value.split('\n');

	if (meows.length !== chars.length) {
		alert(
			`Codebook must contain exactly ${chars.length} lines.`
		);
		return;
	}

	rebuildMaps();
	meowsBox.value = charsToMeows(text.value);
}

text.addEventListener('input', () => {
	meowsBox.value = charsToMeows(text.value);
});

meowsBox.addEventListener('input', () => {
	try {
		text.value = meowsToChars(meowsBox.value);
	} catch {
		text.value = '';
	}
});

codebook.addEventListener('input', () => {
	applyCodebook();
});
