//     Zepto.js
//     (c) 2010-2013 Thomas Fuchs
//     Zepto.js may be freely distributed under the MIT license.
;
(function($) {
	var touch = {},
		touchTimeout, tapTimeout, swipeTimeout, longTapTimeout,
		longTapDelay = 750,
		gesture

		function swipeDirection(x1, x2, y1, y2) {
			return Math.abs(x1 - x2) >=
				Math.abs(y1 - y2) ? (x1 - x2 > 0 ? 'Left' : 'Right') : (y1 - y2 > 0 ? 'Up' : 'Down')
		}

		function longTap() {
			longTapTimeout = null
			if (touch.last) {
				touch.el.trigger('longTap')
				touch = {}
			}
		}

		function cancelLongTap() {
			if (longTapTimeout) clearTimeout(longTapTimeout)
			longTapTimeout = null
		}

		function cancelAll() {
			if (touchTimeout) clearTimeout(touchTimeout)
			if (tapTimeout) clearTimeout(tapTimeout)
			if (swipeTimeout) clearTimeout(swipeTimeout)
			if (longTapTimeout) clearTimeout(longTapTimeout)
			touchTimeout = tapTimeout = swipeTimeout = longTapTimeout = null
			touch = {}
		}

		function isPrimaryTouch(event) {
			return (event.pointerType == 'touch' ||
				event.pointerType == event.MSPOINTER_TYPE_TOUCH) && event.isPrimary
		}

		function isPointerEventType(e, type) {
			return (e.type == 'pointer' + type ||
				e.type.toLowerCase() == 'mspointer' + type)
		}

	$(document).ready(function() {
		var now, delta, deltaX = 0,
			deltaY = 0,
			firstTouch, _isPointerType

		if ('MSGesture' in window) {
			gesture = new MSGesture()
			gesture.target = document.body
		}

		$(document)
			.bind('MSGestureEnd', function(e) {
				var swipeDirectionFromVelocity =
					e.velocityX > 1 ? 'Right' : e.velocityX < -1 ? 'Left' : e.velocityY > 1 ? 'Down' : e.velocityY < -1 ? 'Up' : null;
				if (swipeDirectionFromVelocity) {
					touch.el.trigger('swipe')
					touch.el.trigger('swipe' + swipeDirectionFromVelocity)
				}
			})
			.on('touchstart MSPointerDown pointerdown', function(e) {
				if ((_isPointerType = isPointerEventType(e, 'down')) && !isPrimaryTouch(e)) return
				firstTouch = _isPointerType ? e : e.touches[0]
				if (e.touches && e.touches.length === 1 && touch.x2) {
					// Clear out touch movement data if we have it sticking around
					// This can occur if touchcancel doesn't fire due to preventDefault, etc.
					touch.x2 = undefined
					touch.y2 = undefined
				}
				now = Date.now()
				delta = now - (touch.last || now)
				touch.el = $('tagName' in firstTouch.target ?
					firstTouch.target : firstTouch.target.parentNode)
				touchTimeout && clearTimeout(touchTimeout)
				touch.x1 = firstTouch.pageX
				touch.y1 = firstTouch.pageY
				if (delta > 0 && delta <= 250) touch.isDoubleTap = true
				touch.last = now
				longTapTimeout = setTimeout(longTap, longTapDelay)
				// adds the current touch contact for IE gesture recognition
				if (gesture && _isPointerType) gesture.addPointer(e.pointerId);
			})
			.on('touchmove MSPointerMove pointermove', function(e) {
				if ((_isPointerType = isPointerEventType(e, 'move')) && !isPrimaryTouch(e)) return
				firstTouch = _isPointerType ? e : e.touches[0]
				cancelLongTap()
				touch.x2 = firstTouch.pageX
				touch.y2 = firstTouch.pageY

				deltaX += Math.abs(touch.x1 - touch.x2)
				deltaY += Math.abs(touch.y1 - touch.y2)
			})
			.on('touchend MSPointerUp pointerup', function(e) {
				if ((_isPointerType = isPointerEventType(e, 'up')) && !isPrimaryTouch(e)) return
				cancelLongTap()

				// swipe
				if ((touch.x2 && Math.abs(touch.x1 - touch.x2) > 30) ||
					(touch.y2 && Math.abs(touch.y1 - touch.y2) > 30))

					swipeTimeout = setTimeout(function() {
						touch.el.trigger('swipe')
						touch.el.trigger('swipe' + (swipeDirection(touch.x1, touch.x2, touch.y1, touch.y2)))
						touch = {}
					}, 0)

				// normal tap
				else if ('last' in touch)
				// don't fire tap when delta position changed by more than 30 pixels,
				// for instance when moving to a point and back to origin
					if (deltaX < 30 && deltaY < 30) {
						// delay by one tick so we can cancel the 'tap' event if 'scroll' fires
						// ('tap' fires before 'scroll')
						tapTimeout = setTimeout(function() {

							// trigger universal 'tap' with the option to cancelTouch()
							// (cancelTouch cancels processing of single vs double taps for faster 'tap' response)
							var event = $.Event('tap')
							event.cancelTouch = cancelAll
							touch.el.trigger(event)

							// trigger double tap immediately
							if (touch.isDoubleTap) {
								if (touch.el) touch.el.trigger('doubleTap')
								touch = {}
							}

							// trigger single tap after 250ms of inactivity
							else {
								touchTimeout = setTimeout(function() {
									touchTimeout = null
									if (touch.el) touch.el.trigger('singleTap')
									touch = {}
								}, 250)
							}
						}, 0)
					} else {
						touch = {}
					}
				deltaX = deltaY = 0

			})
		// when the browser window loses focus,
		// for example when a modal dialog is shown,
		// cancel all ongoing events
		.on('touchcancel MSPointerCancel pointercancel', cancelAll)

		// scrolling the window indicates intention of the user
		// to scroll, not tap or swipe, so cancel all ongoing events
		$(window).on('scroll', cancelAll)
	})

	;
	['swipe', 'swipeLeft', 'swipeRight', 'swipeUp', 'swipeDown',
		'doubleTap', 'tap', 'singleTap', 'longTap'
	].forEach(function(eventName) {
		$.fn[eventName] = function(callback) {
			return this.on(eventName, callback)
		}
	})
})(Zepto);
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
			E_floatOk.off('tap').on('tap', function(e) {
				callback.call(that, e, true);
			});
			E_floatCancel.off('tap').on('tap', function(e) {
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
    'PASSWORD_LENGTH': '密码不能少于6位或大于11位',
    'TEL_PATTERN_ERROR': '请输入正确的手机号',
    'EMAIL_PATTERN_ERROR': '请输入正确邮箱',
	'OLDPWD_EMPTY': '旧密码不能为空',
	'NEWPWD_EMPTY': '新密码不能为空',
	'REPWD_EMPTY': '确认密码不能为空',
	'PWD_EQUEL': '两次新密码不一致',
	'ACCOUNT_EXIST': '账号已存在',
	'REGISTER_SUCCESS': '注册成功',
	'ACCOUNT_PASSWORD_ERROR': '用户名或密码错误',
	'REAL_NAME_EMPTY': '真实姓名不能为空',
	'EMAIL_EMPTY': '邮箱不能为空',
	'TEL_EMPTY': '手机号不能为空',
	'KIND_EMPTY': '种类不能为空',
	'ENERGY_EMPTY': '能量不能为空',
	'PROTEIN_EMPTY': '蛋白质不能为空',
	'TSHHEW_EMPTY': '碳化学物不能为空',
	'FAT_EMPTY': '脂肪不能为空',
	'PATRIARCH_EMPTY': '家长手机号不能为空',
	'BABY_NAME_EMPTY': '婴儿名不能为空',
	'GENDER_EMPTY': '性别不能为空',
	'DUE_DATE_EMPTY': '预产期不能为空',
	'BIRTHDAY_EMPTY': '出生日期不能为空',
	'WEIGHT_EMPTY': '体重不能为空',
	'HEIGHT_EMPTY': '身长不能为空',
	'HEAD_EMPTY': '头围不能为空',
	'CHILDBIRTH_EMPTY': '分娩方式不能为空',
	'COMPLICATION_EMPTY': '合并症不能为空',
	'DATE_EMPTY': '测量日期不能为空',
	'FEEDING_EMPTY': '母乳喂养不能为空',
	'OLD_PASSWORD_ERROR': '旧密码不正确',
    'CHANGE_PASSWORD_SUCCESS': '修改密码成功',
    'PLEASE_CHECKED': '请确认注册协议',
	'LOGIN_URL': '/restful/html/do/login',
	'FORGET_PWD': '/restful/html/forget/password',
	'REGISTER_URL': '/restful/html/do/register',
	'MILK_URL': '/restful/html/add/formula',
	'CREATE_BABY_URL': '/restful/html/create/baby',
	'ADD_VISIT_URL': '/restful/html/add/visit'
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
				'remember': rememberCheckbox.attr('checked') ? 1 : 0,
                'login_type': 'doctor'
			}
			MZ.util.Request({
				url: MZ.constant.LOGIN_URL,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': '登陆成功'
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						var doctorList = json.doctor_list
						// 调用java方法
						window.app.webviewLogin(doctorList.user_id, doctorList.is_remember, doctorList.user_name)
					}, 2000)
				} else {
					window.Notification.simple(MZ.constant.ACCOUNT_PASSWORD_ERROR, 2000)
					return
				}
			})

		})
	},
    mummyLogin: function() {
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
				'remember': rememberCheckbox.attr('checked') ? 1 : 0,
                'login_type': 'mummy'
			}
			MZ.util.Request({
				url: MZ.constant.LOGIN_URL,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': '登陆成功'
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						var doctorList = json.doctor_list
						// 调用java方法
						window.app.webviewLogin(doctorList.user_id, doctorList.is_remember, doctorList.user_name)
					}, 2000)
				} else {
					window.Notification.simple(MZ.constant.ACCOUNT_PASSWORD_ERROR, 2000)
					return
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
            if (oldPwdValue.length < 6 || oldPwdValue.length > 11){
                window.Notification.simple(MZ.constant.PASSWORD_LENGTH, 2000)
                return
            }
            if (newPwdValue.length < 6 || newPwdValue.length > 11){
                window.Notification.simple(MZ.constant.PASSWORD_LENGTH, 2000)
                return
            }
			var params = {
				'old_password': oldPwdValue,
				'new_password': newPwdValue
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
                    window.Notification.simple(MZ.constant.CHANGE_PASSWORD_SUCCESS)
					setTimeout(function() {
						// 调用java方法
						window.app.webviewPassword(json.code)
						// where to go ?
					}, 2000)
				} else if (code === 500) {
					window.Notification.simple(MZ.constant.OLD_PASSWORD_ERROR, 2000)
					return
				}
			})

		})

	},
	register: function() {
		var user_name = $('#login_name')
		var user_pass = $('#login_pass')
		var confirm_pass = $('#confirm')
		var real_name = $('#real_name')
		var province = $('#province')
		var hospital = $('#belong-hospital')
		var department = $('#belong-department')
		var position = $('#position')
		var email = $('#email')
		var tel = $('#tel')
		var registerBtn = $('#register-btn')
        var registerAgree = $("#register-agree")
        var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
        var tel_reg = /^1[3|4|5|8][0-9]\d{4,8}$/;

		registerBtn.bind('click', function() {
			var checkUserName = MZ.app.checkField(user_name)
			var checkNewPwd = MZ.app.checkField(user_pass)
			var checkConfirm = MZ.app.checkField(confirm_pass)
			var checkRealName = MZ.app.checkField(real_name)
			var checkEmail = MZ.app.checkField(email)
			var checkTel = MZ.app.checkField(tel)
			if (!checkUserName) {
				window.Notification.simple(MZ.constant.USERNAME_EMPTY, 2000)
				return
			}
			if (!checkNewPwd) {
				window.Notification.simple(MZ.constant.PASSWORD_EMPTY, 2000)
				return
			}
			if (!checkConfirm) {
				window.Notification.simple(MZ.constant.REPWD_EMPTY, 2000)
				return
			}
			if (!checkRealName) {
				window.Notification.simple(MZ.constant.REAL_NAME_EMPTY, 2000)
				return
			}
			if (!checkEmail) {
				window.Notification.simple(MZ.constant.EMAIL_EMPTY, 2000)
				return
			}
			if (!checkTel) {
				window.Notification.simple(MZ.constant.TEL_EMPTY, 2000)
				return
			}
            if (!registerAgree.is(":checked")){
                window.Notification.simple(MZ.constant.PLEASE_CHECKED, 2000)
                return
            }
			var userNameValue = $.trim(user_name.val())
			var userPassValue = $.trim(user_pass.val())
			var rePwdValue = $.trim(confirm_pass.val())
			var realNameValue = $.trim(real_name.val())
			var provinceValue = $.trim(province.val())
			var hospitalValue = $.trim(hospital.val())
			var departmentValue = $.trim(department.val())
			var positionValue = $.trim(position.val())
			var emailValue = $.trim(email.val())
			var telValue = $.trim(tel.val())

			if (userPassValue != rePwdValue) {
				window.Notification.simple(MZ.constant.PWD_EQUEL, 2000)
				return
			}
            if (userPassValue.length < 6 || userPassValue.length > 11){
                window.Notification.simple(MZ.constant.PASSWORD_LENGTH, 2000)
                return
            }
            if (!reg.test(emailValue)){
                window.Notification.simple(MZ.constant.EMAIL_PATTERN_ERROR, 2000)
                return
            }
            if (!tel_reg.test(telValue)){
                window.Notification.simple(MZ.constant.TEL_PATTERN_ERROR, 2000)
                return
            }

			var params = {
				'login_name': userNameValue,
				'login_pass': userPassValue,
				'real_name': realNameValue,
				'province_id': provinceValue,
				'belong_hospital': hospitalValue,
				'belong_department': departmentValue,
				'position': positionValue,
				'email': emailValue,
				'tel': telValue
			}
			MZ.util.Request({
				url: MZ.constant.REGISTER_URL,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': json.msg
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						// 调用java方法
						window.app.webviewRegister(json.code, json.doctor_id)
						// where to go ?
					}, 2000)
					window.Notification.simple(MZ.constant.REGISTER_SUCCESS, 2000)
				} else {
					window.Notification.simple(MZ.constant.ACCOUNT_EXIST, 2000)
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

		arrowLeftElem.on('tap', function() {
			navElem.iScroll('scrollTo', -100, 0, 400, true)
		})

		arrowRightElem.on('tap', function() {
			navElem.iScroll('scrollTo', 100, 0, 400, true)
		})
	},
	checkRadio: function(ele) {
		var radio = $(ele);
		radio.on('click', function() {
			$(this).addClass('checked').find('input[type="radio"]').attr('checked', 'checked');
			$(this).parent().siblings('li').find('.iradio').removeClass('checked').find('input[type="radio"]')
				.attr('checked', null);
		});
	},
	formulaSubmit: function(ele) {
		var subBtn = $(ele).find('.submit');
		var kind = $(ele).find('#l-kind');
		var energy = $(ele).find('#l-energy');
		var protein = $(ele).find('#l-protein');
		var carbohydrates = $(ele).find('#l-carbohydrates');
		var fat = $(ele).find('#l-fat');
		var checkedFun = function(){ return this.checked; }

		subBtn.bind('click', function() {
			var location = $(ele).find('input[type="radio"][name="location"]').filter(checkedFun).val();
			var brand = $(ele).find('input[type="radio"][name="brand"]').filter(checkedFun).val();
			var checkKind = MZ.app.checkField(kind)
			var checkEnergy = MZ.app.checkField(energy)
			var checkProtein = MZ.app.checkField(protein)
			var checkTshhw = MZ.app.checkField(carbohydrates)
			var checkFat = MZ.app.checkField(fat)
            var divDisplayObj = $("#div-display")

            if (divDisplayObj.display = 'none'){
                if (!checkKind) {
                    window.Notification.simple(MZ.constant.KIND_EMPTY, 2000)
                    return
                }
            } else{
                if (!checkKind) {
                    window.Notification.simple(MZ.constant.KIND_EMPTY, 2000)
                    return
                }
                if (!checkEnergy) {
                    window.Notification.simple(MZ.constant.ENERGY_EMPTY, 2000)
                    return
                }
                if (!checkProtein) {
                    window.Notification.simple(MZ.constant.PROTEIN_EMPTY, 2000)
                    return
                }
                if (!checkTshhw) {
                    window.Notification.simple(MZ.constant.TSHHEW_EMPTY, 2000)
                    return
                }
                if (!checkFat) {
                    window.Notification.simple(MZ.constant.FAT_EMPTY, 2000)
                    return
                }
            }


			var params = {
				'court_id': location,
				'brand_id': brand,
				'kind': $.trim(kind.val()),
				'energy': $.trim(energy.val()),
				'protein': $.trim(protein.val()),
				'carbohydrates': $.trim(carbohydrates.val()),
				'fat': $.trim(fat.val())
			}
			MZ.util.Request({
				url: MZ.constant.MILK_URL,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': json.msg
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						// 调用java方法
						window.app.webviewFormula(json.code)
						// where to go ?
					}, 2000)
				}
			})
		})
	},

	addVisitSubmit: function(ele) {
		var subBtn = $(ele).find('.submit');
		var cdate = $(ele).find('#l-checkdate');
		var weight = $(ele).find('#l-weight');
		var height = $(ele).find('#l-height');
		var head = $(ele).find('#l-head');
		var feeding = $(ele).find('#l-breastfeeding');
		var baby_id = $(ele).find('#baby_id')

		subBtn.bind('tap', function() {
			var location = $(ele).find('#l-location').val();
			var brand = $(ele).find('#l-brand').val();
			var kind = $(ele).find('#l-kind').val();
			var nutrition = $(ele).find('#l-nutrition').val();
			var checkDate = MZ.app.checkField(cdate);
			var checkWeight = MZ.app.checkField(weight);
			var checkHeight = MZ.app.checkField(height);
			var checkHead = MZ.app.checkField(head);
			var checkFeeding = MZ.app.checkField(feeding);

			if (!checkDate) {
				window.Notification.simple(MZ.constant.DATE_EMPTY, 2000)
				return
			}
			if (!checkWeight) {
				window.Notification.simple(MZ.constant.WEIGHT_EMPTY, 2000)
				return
			}
			if (!checkHeight) {
				window.Notification.simple(MZ.constant.HEIGHT_EMPTY, 2000)
				return
			}
			if (!checkHead) {
				window.Notification.simple(MZ.constant.HEAD_EMPTY, 2000)
				return
			}
			if (!checkFeeding) {
				window.Notification.simple(MZ.constant.FEEDING_EMPTY, 2000)
				return
			}
			var params = {
				'measure_date': cdate.val(),
				'weight': $.trim(weight.val()),
				'height': $.trim(height.val()),
				'head': $.trim(head.val()),
				'breastfeeding': $.trim(feeding.val()),
				'nutrition': nutrition,
				'location': location,
				'brand': brand,
				'kind': kind,
				'baby_id': $.trim(baby_id.val())
			};
			MZ.util.Request({
				url: MZ.constant.ADD_VISIT_URL,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': json.msg
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						// 调用java方法
						window.app.webviewAddVisit(json.code)
						// where to go ?
					}, 2000)
				}
			})
		})
	},
	createBabyAccount: function(ele) {
		var subBtn = $(ele).find('#z-create');
		var complication = $(ele).find('#z-complication');
		var childbirth = $(ele).find('#z-childbirth');
		var head = $(ele).find('#z-head');
		var height = $(ele).find('#z-height');
		var patriarch = $(ele).find('#z-patriarch-tel');
		var babyName = $(ele).find('#z-baby-name');
		var password = $(ele).find('#z-password');
		var confirmPassword = $(ele).find('#z-confirm-password');
		var gender = $(ele).find('#z-gender');
		var dueDate = $(ele).find('#z-due-date');
		var birthday = $(ele).find('#z-birthday');
		var weight = $(ele).find('#z-weight');
		var height = $(ele).find('#z-height');
		var head = $(ele).find('#z-head');

		subBtn.bind('click', function() {
			var checkPatriarch = MZ.app.checkField(patriarch);
			var checkBabyName = MZ.app.checkField(babyName);
			var checkPassword = MZ.app.checkField(password);
			var checkConfirmPassword = MZ.app.checkField(confirmPassword);
			var checkWeight = MZ.app.checkField(weight);
			var checkHeight = MZ.app.checkField(height);
			var checkHead = MZ.app.checkField(head);

			if (!checkPatriarch) {
				window.Notification.simple(MZ.constant.PATRIARCH_EMPTY, 2000)
				return
			}
			if (!checkBabyName) {
				window.Notification.simple(MZ.constant.BABY_NAME_EMPTY, 2000)
				return
			}
			if (!checkPassword) {
				window.Notification.simple(MZ.constant.PASSWORD_EMPTY, 2000)
				return
			}
			if (!checkConfirmPassword) {
				window.Notification.simple(MZ.constant.REPWD_EMPTY, 2000)
				return
			}
			if (!checkWeight) {
				window.Notification.simple(MZ.constant.WEIGHT_EMPTY, 2000)
				return
			}
			if (!checkHeight) {
				window.Notification.simple(MZ.constant.HEIGHT_EMPTY, 2000)
				return
			}
			if (!checkHead) {
				window.Notification.simple(MZ.constant.HEAD_EMPTY, 2000)
				return
			}
			var patriarchValue = $.trim(patriarch.val())
			var babyNameValue = $.trim(babyName.val())
			var passwordValue = $.trim(password.val())
			var confirmPasswordValue = $.trim(confirmPassword.val())
			var genderValue = $.trim(gender.val())
			var dueDateValue = $.trim(dueDate.val())
			var birthdayValue = $.trim(birthday.val())
			var weightValue = $.trim(weight.val())
			var heightValue = $.trim(height.val())
			var headValue = $.trim(head.val())
			var childbirthValue = $.trim(childbirth.val())
			var complicationValue = $.trim(complication.val())

			if (passwordValue != confirmPasswordValue) {
				window.Notification.simple(MZ.constant.PWD_EQUEL, 2000)
				return
			}

			var params = {
				'patriarch_tel': patriarchValue,
				'baby_name': babyNameValue,
				'baby_pass': passwordValue,
				'gender': genderValue,
				'due_date': dueDateValue,
				'born_birthday': birthdayValue,
				'born_weight': weightValue,
				'born_height': heightValue,
				'born_head': headValue,
				'childbirth_style_id': childbirthValue,
				'complication_id': complicationValue
			};
			MZ.util.Request({
				url: MZ.constant.CREATE_BABY_URL,
				data: params
			}, function(json) {
				var code = json.code
				Notification.pop({
					'text': json.msg
				}).flash(2000)
				if (code === 200) {
					setTimeout(function() {
						// 调用java方法
						window.app.webviewCreateBaby(json.code)
						// where to go ?
					}, 2000)
				} else {
					window.Notification.simple(MZ.constant.ACCOUNT_EXIST, 2000)
					return
				}
			})
		})
	}
}