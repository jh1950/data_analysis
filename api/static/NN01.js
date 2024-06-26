window.addEventListener("DOMContentLoaded", function() {
	const config = {
		type: "line",
		data: {
			labels: [],
			datasets: [{
				label: "Random Dataset",
				backgroundColor: 'rgb(255, 99, 132)',
				borderColor: 'rgb(255, 99, 132)',
				data: [],
				fill: false,
			}],
		},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Creating Real-Time Charts with FastAPI'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Time'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Value'
					}
				}]
			}
		}
	};

	const context = document.querySelector("#canvas").getContext('2d');
	const lineChart = new Chart(context, config);
	const source = new EventSource("/NN01/fakeStream");
	source.onmessage = function(event) {
		const data = JSON.parse(event.data);
		if (config.data.labels.length === 20) {
			config.data.labels.shift();
			config.data.datasets[0].data.shift();
		}
		config.data.labels.push(data.time);
		config.data.datasets[0].data.push(data.value);
		lineChart.update();
	}
});
