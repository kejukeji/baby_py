$(function() {
	var w2 = weightObj.data[0];
	var w3 = weightObj.data[1];
	var t;
	var data = [{
		name: 'WHO',
		value: w2,
		color: '#0d8ecf',
		line_width: 1
	}, {
		name: 'SH',
		value: w3,
		color: '#6db284',
		line_width: 1
	}];

	var labels = weightObj.xAxis;

	var chart = new iChart.LineBasic2D({
		render: 'canvasDiv',
		data: data,
		align: 'center',
		fit: false,
		shadow: false,
		width: $('.chart-frame').width(),
		height: 300,
		border: 0,
		turn_off_touchmove: true,
		//background_color: '#0391d5',
		sub_option: {
			smooth: true,
			label: true,
			hollow: false,
			hollow_inside: false,
			point_size: 1
		},
		legend: {
			enable: true,
			row: 1, //设置在一行上显示，与column配合使用
			column: 'max',
			valign: 'top',
			sign: 'bar',
			background_color: null, //设置透明背景
			offsetx: -10, //设置x轴偏移，满足位置需要
			offsety: -10,
			border: true
		},
		coordinate: {
			grid_color: '#c8c8c8',
			axis: {
				color: '#ccc',
				width: [0, 0, 0, 0]
			},
			scale: [{
				position: 'left',
				start_scale: weightObj.yStart,
				end_scale: weightObj.yEnd,
				scale_space: weightObj.ySpace,
				scale_size: 1,
				scale_enable: false,
				label: {
					color: '#323232',
					fontsize: 10
				},
				scale_color: '#000'
			}, {
				position: 'bottom',
				label: {
					color: '#323232',
					fontsize: 10,
				},
				scale_enable: false,
				labels: labels
			}]
		}
	});
	//利用自定义组件构造左侧说明文本
	chart.plugin(new iChart.Custom({
		drawFn: function() {
			//计算位置
			var coo = chart.getCoordinate(),
				x = coo.get('originx'),
				y = coo.get('originy'),
				w = coo.width,
				h = coo.height;
			//在左上侧的位置，渲染一个单位的文字
			chart.target.textAlign('start')
				.textBaseline('bottom')
				.textFont('400 10px');
		}
	}));
	chart.on('beforedraw', function(e) {
		chart.START_RUN_TIME = new Date().getTime();
		return true;
	});

	chart.on('draw', function(e) {
		chart.END_RUN_TIME = new Date().getTime();
		chart.RUN_TIME_COST = chart.END_RUN_TIME - chart.START_RUN_TIME;
	});
	//开始画图
	chart.draw();

	$(window).resize(function() {
		chart.resize($('.chart-frame').width(), 300);
	});
});