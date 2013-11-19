/*-------------------------------------------------
     MZ Namespace
-------------------------------------------------*/
var MZ = window.MZ || {};
MZ.namespace = function() {
	var a = arguments,
		o = null,
		i, j, d;
	for (i = 0; i < a.length; ++i) {
		d = a[i].split('.');
		o = MZ;
		for (j = (d[0] === 'MZ') ? 1 : 0; j < d.length; ++j) {
			o[d[j]] = o[d[j]] || {};
			o = o[d[j]];
		}
	}
	return o;
};
MZ.namespace('util');
MZ.namespace('constant');
MZ.namespace('Cookie');
/*-------------------------------------------------
     MZ Utils
-------------------------------------------------*/
MZ.util = {
	// 数组去重
	uniqArray: function(arr) {
		var a = [],
			o = {}, i, v,
			len = arr.length;
		if (len < 2) {
			return arr;
		}
		for (i = 0; i < len; i++) {
			v = arr[i];
			if (o[v] !== 1) {
				a.push(v);
				o[v] = 1;
			}
		}
		return a;
	},
	// 浏览器是否支持地理地位
	isGeolocationSupported: function() {
		return navigator.geolocation ? true : false;
	},
	// 浏览器是否支持本地存储
	isLocalStorageSupported: function() {
		try {
			return 'localStorage' in window && window['localStorage'] !== null;
		} catch (e) {
			return false;
		}
	},
	Request: function(options, cb) {
		var defaults = {
			type: 'POST',
			url: '',
			async: true,
			data: {},
			dataType: 'json',
			timeout: 3000,
			success: function(data) {
				cb(data);
			},
			error: function(xhr, type) {
				alert('请求失败，请重新尝试!');
				//Notification.pop({
				//	'text': '请求失败，请重新尝试!'
				//}).flash(2000);
			}
		};
		var opt = $.extend(defaults, options);
		$.ajax(opt);
	}
};
/*-------------------------------------------------
     MZ Cookies(get && set)
-------------------------------------------------*/
MZ.Cookie = {
	set: function(name, value, expire, path) {
		var exp = new Date();
		exp.setTime(exp.getTime() + expire * 60 * 1000);
		document.cookie = name + "=" + encodeURIComponent(value) + ";expires=" + exp.toGMTString() + ";domain=" + document.domain.substring(1) + ";path=" + path + ";";
	},
	get: function(name) {
		var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
		if (arr != null) return decodeURIComponent(arr[2]);
		return null;
	}
};
/*-------------------------------------------------
     MZ.app Namespace (for Business Code)
-------------------------------------------------*/
MZ.namespace('app');
/*------------------------------------------------
 * lazyload , extend Zepto, based on unveil.js
 * --------------------------------------------*/
(function($) {
	$.fn.unveil = function(threshold) {
		if (!this.size()) {
			return;
		}
		var $w = $(window),
			th = threshold || 0,
			retina = window.devicePixelRatio > 1,
			attrib = retina ? "data-src-retina" : "data-src",
			images = this,
			loaded,
			inview,
			source;
		this.one("unveil", function() {
			source = this.getAttribute(attrib);
			source = source || this.getAttribute("data-src");
			if (source) {
				this.setAttribute("src", source);
			}
		});

		function unveil() {
			inview = images.filter(function() {
				var $e = $(this),
					wt = $w.scrollTop(),
					wb = wt + $w.height(),
					et = $e.offset().top,
					eb = et + $e.height();
				return eb >= wt - th && et <= wb + th;
			});
			loaded = inview.trigger("unveil");
			images = images.not(loaded);
		}
		$w.scroll(unveil);
		$w.resize(unveil);
		unveil();
		return this;
	};
})(window.Zepto);
(function($) {
	var win = $(window);
	var T_float = ['<div class="c-float-popWrap msgMode hide">', '<div class="c-float-modePop">', '<div class="warnMsg"></div>', '<div class="content"></div>', '<div class="doBtn hide">', '<button class="ok">确定</button>', '<button class="cancel">取消</button>', '</div>', '</div>', '</div>'].join('');
	var E_float = $(T_float);
	var E_floatMsg = E_float.find('.warnMsg');
	var E_floatContent = E_float.find('.content');
	var E_floatOk = E_float.find('.doBtn .ok');
	var E_floatCancel = E_float.find('.doBtn .cancel');
	var initDom = false;
	var domContainer = 'body';
	var flashTimeoutId;

	function ModePop(options) {
		this._options = $.extend({
			mode: 'msg',
			text: '网页提示',
		}, options || {});
		this._init();
	}
	$.extend(ModePop.prototype, {
		_init: function() {
			var that = this,
				opt = that._options,
				mode = opt.mode,
				text = opt.text,
				content = opt.content,
				callback = opt.callback,
				background = opt.background;
			// set mode
			var classTxt = E_float.attr('class');
			classTxt = classTxt.replace(/(msg|alert|confirm)Mode/i, mode + 'Mode');
			E_float.attr('class', classTxt);
			// set background
			background && E_float.css('background', background);
			// set text & content
			text && E_floatMsg.html(text);
			content && E_floatContent.html(content);
			// click event
			/*
                                 E_float.off('click')
                                 .on('click', '.doBtn .ok', function(e) {
                                 callback.call(that, e, true);
                                 })
                                 .on('click', '.doBtn .cancel', function(e) {
                                 callback.call(that, e, false);
                                 });
                                 */
			E_floatOk.off('click').on('click', function(e) {
				callback.call(that, e, true);
			});
			E_floatCancel.off('click').on('click', function(e) {
				callback.call(that, e, false);
			});
			if (!initDom) {
				initDom = true;
				$(domContainer).append(E_float);
				win.on('resize', function() {
					setTimeout(function() {
						that._pos();
					}, 500);
				});
			}
		},
		_pos: function() {
			var that = this,
				doc = document,
				docEl = doc.documentElement,
				body = doc.body,
				top, left, cW, cH, eW, eH;
			if (!that.isHide()) {
				top = body.scrollTop;
				left = body.scrollLeft;
				cW = docEl.clientWidth;
				cH = docEl.clientHeight;
				eW = E_float.width();
				eH = E_float.height();
				E_float.css({
					top: top + (cH - eH) / 2,
					left: left + (cW - eW) / 2
				});
			}
		},
		isShow: function() {
			return E_float.hasClass('show');
		},
		isHide: function() {
			return E_float.hasClass('hide');
		},
		_cbShow: function() {
			var that = this,
				opt = that._options,
				onShow = opt.onShow;
			E_float.addClass('show');
			// 特殊处理
			var overlayEle = $('.pop-main-wrap');
			if (overlayEle.size() > 0) {
				overlayEle.removeClass('hide');
			} else {
				$(domContainer).append('<div class="pop-main-wrap"></div>');
			}
			onShow && onShow.call(that);
		},
		show: function() {
			var that = this;
			if (flashTimeoutId) {
				clearTimeout(flashTimeoutId);
				flashTimeoutId = undefined;
			}
			if (!that.isShow()) {
				E_float.css('opacity', '0').removeClass('hide');
				that._pos();
				E_float.animate({
					'opacity': '1'
				}, 300, 'linear', function() {
					that._cbShow();
				});
			} else {
				that._cbShow();
			}
		},
		_cbHide: function() {
			var that = this,
				opt = that._options,
				onHide = opt.onHide;
			E_float.addClass('hide');
			$('.pop-main-wrap').addClass('hide');
			onHide && onHide.call(that);
		},
		hide: function() {
			var that = this;
			if (!that.isHide()) {
				E_float.css('opacity', 1).removeClass('show');
				E_float.animate({
					'opacity': 0
				}, 300, 'linear', function() {
					that._cbHide();
				});
			} else {
				that._cbHide();
			}
		},
		flash: function(timeout) {
			var that = this
			opt = that._options;
			opt.onShow = function() {
				flashTimeoutId = setTimeout(function() {
					if (flashTimeoutId) {
						that.hide();
					}
				}, timeout);
			}
			that.show();
		}
	});
	window.Notification = new function() {
		this.simple = function(text, bg, timeout) {
			if (arguments.length == 2) {
				if (typeof arguments[1] == 'number') {
					timeout = arguments[1];
					bg = undefined;
				}
			}
			var pop = new ModePop({
				mode: 'msg',
				text: text,
				background: bg
			});
			pop.flash(timeout || 2000);
			return pop;
		}
		this.msg = function(text, options) {
			return new ModePop($.extend({
				mode: 'msg',
				text: text
			}, options || {}));
		}
		this.alert = function(text, callback, options) {
			return new ModePop($.extend({
				mode: 'alert',
				text: text,
				callback: callback
			}, options || {}));
		}
		this.confirm = function(text, content, callback, options) {
			return new ModePop($.extend({
				mode: 'confirm',
				text: text,
				content: content,
				callback: callback,
			}, options || {}));
		}
		this.pop = function(options) {
			return new ModePop(options);
		}
	};
})(window.Zepto);
MZ.constant = {
	'USERNAME_EMPTY': '用户名不能为空',
	'PASSWORD_EMPTY': '密码不能为空',
	'OLDPWD_EMPTY': '旧密码不能为空',
	'NEWPWD_EMPTY': '新密码不能为空',
	'REPWD_EMPTY': '确认密码不能为空',
	'PWD_EQUEL': '两次新密码不一致',
	// 'LOGIN_URL': 'json/login.json',
	'LOGIN_URL': '/restful/html/do/login',
	'FORGET_PWD': 'json/password.json'
}

MZ.app = {
	checkField: function(elem) {
		var elemStr = $.trim($(elem).val())
		if (!elemStr.length) {
			return false
		}
		return true
	},
	login: function() {
		var login_btn = $('#L-login-btn')
		var username = $('#L-username')
		var password = $('#L-password')
		var rememberCheckbox = $('#L-remember')

		login_btn.bind('click', function() {
			var checkUsername = MZ.app.checkField(username)
			var checkPassword = MZ.app.checkField(password)
			if (!checkUsername) {
				window.Notification.simple(MZ.constant.USERNAME_EMPTY, 2000)
				return
			}
			if (!checkPassword) {
				window.Notification.simple(MZ.constant.PASSWORD_EMPTY, 2000)
				return
			}
			var params = {
				'login_name': $.trim(username.val()),
				'login_pass': $.trim(password.val()),
				'remember': rememberCheckbox.attr('checked') ? 1 : 0
			}
			MZ.util.Request({
				url: MZ.constant.LOGIN_URL,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': json.msg
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						var doctorList = json.doctor_list
						// 调用java方法
						window.app.webviewLogin(json.doctor_list.user_id, json.doctor_list.is_remember)
					}, 2000)
				}
			})

		})
	},
	password: function() {
		var oldPassword = $('#L-old-password')
		var newPassword = $('#L-new-password')
		var rePassword = $('#L-re-password')
		var saveBtn = $('#L-save')

		saveBtn.bind('click', function() {
			var checkOldPwd = MZ.app.checkField(oldPassword)
			var checkNewPwd = MZ.app.checkField(newPassword)
			var checkRePwd = MZ.app.checkField(rePassword)
			if (!checkOldPwd) {
				window.Notification.simple(MZ.constant.OLDPWD_EMPTY, 2000)
				return
			}
			if (!checkNewPwd) {
				window.Notification.simple(MZ.constant.NEWPWD_EMPTY, 2000)
				return
			}
			if (!checkRePwd) {
				window.Notification.simple(MZ.constant.REPWD_EMPTY, 2000)
				return
			}
			var oldPwdValue = $.trim(oldPassword.val())
			var newPwdValue = $.trim(newPassword.val())
			var rePwdValue = $.trim(rePassword.val())

			if (newPwdValue != rePwdValue) {
				window.Notification.simple(MZ.constant.PWD_EQUEL, 2000)
				return
			}
			var params = {
				'oldPassword': oldPwdValue,
				'newPassword': newPwdValue
			}
			MZ.util.Request({
				url: MZ.constant.FORGET_PWD,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': json.msg
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						// 调用java方法
						// window.webviewPassword(json.userId)
						// where to go ?
					}, 2000)
				}
			})

		})

	},
	slideNavigator: function() {
		var bar = $('#L-nav span.bar')
		var left = $('#L-nav ul').offset().left
		var navElem = $('#L-nav')
		var arrowLeftElem = $('#L-arrow-left')
		var arrowRightElem = $('#L-arrow-right')
		navElem.navigator({
			select: function(e, index, li) {
				bar.css({
					left: li.offsetLeft - left,
					width: li.childNodes[0].offsetWidth
				})
			},
			ready: function() {
				bar.appendTo(navElem.find('.ui-scroller'));
			}
		})

		arrowLeftElem.on('click', function() {
			navElem.iScroll('scrollTo', -100, 0, 400, true)
		})

		arrowRightElem.on('click', function() {
			navElem.iScroll('scrollTo', 100, 0, 400, true)
		})
	}
}