/*
(Built: Tue, Nov 17, 2015 12:08:58 PM)
Marmoset Viewer Code and Tools

Copyright (c) 2015 Marmoset LLC.
All rights reserved.

Redistribution and use of this software are permitted provided
that the software remains whole and unmodified and this copyright
notice remains attached. Use or inclusion of any portion of this
code in other software programs is prohibited, excepting simple
embedding of this file in web applications. This software, or any
derivatives thereof, may not be resold, rented, leased, or
distributed on any other for-charge basis.

THIS SOFTWARE IS PROVIDED "AS IS" AND WITHOUT ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
*/
marmoset = {};
(function(marmoset) {
    'use strict';

    function Archive(a) {
        this.files = [];
        for (a = new ByteStream(a); !a.empty();) {
            var b = {};
            b.name = a.readCString();
            b.type = a.readCString();
            var c = a.readUint32(),
                d = a.readUint32(),
                e = a.readUint32();
            b.data = a.readBytes(d);
            if (!(b.data.length < d)) {
                if (c & 1 && (b.data = this.decompress(b.data, e), null === b.data)) continue;
                this.files[b.name] = b
            }
        }
    }
    Archive.prototype.get = function(a) {
        return this.files[a]
    };
    Archive.prototype.extract = function(a) {
        var b = this.files[a];
        delete this.files[a];
        return b
    };
    Archive.prototype.checkSignature = function(a) {
        if (!a) return !1;
        var b = this.get(a.name + ".sig");
        if (!b) return !1;
        b = JSON.parse(String.fromCharCode.apply(null, b.data));
        if (!b) return !1;
        for (var c = 5381, d = 0; d < a.data.length; ++d) c = 33 * c + a.data[d] & 4294967295;
        a = new BigInt;
        a.setBytes([0, 233, 33, 170, 116, 86, 29, 195, 228, 46, 189, 3, 185, 31, 245, 19, 159, 105, 73, 190, 158, 80, 175, 38, 210, 116, 221, 229, 171, 134, 104, 144, 140, 5, 99, 255, 208, 78, 248, 215, 172, 44, 79, 83, 5, 244, 152, 19, 92, 137, 112, 10, 101, 142, 209, 100, 244, 92, 190, 125, 28, 0, 185, 54, 143, 247, 49,
            37, 15, 254, 142, 180, 185, 232, 50, 219, 11, 186, 106, 116, 78, 212, 10, 105, 53, 26, 14, 181, 80, 47, 87, 213, 182, 19, 126, 151, 86, 109, 182, 224, 37, 135, 80, 59, 22, 93, 125, 68, 214, 106, 209, 152, 235, 157, 249, 245, 48, 76, 203, 0, 0, 95, 200, 246, 243, 229, 85, 79, 169
        ], !0);
        d = new BigInt;
        d.setBytes(b[0]);
        return d.powmod(65537, a).toInt32() != c ? !1 : !0
    };
    Archive.prototype.decompress = function(a, b) {
        var c = new Uint8Array(b),
            d = 0,
            e = new Uint32Array(4096),
            f = new Uint32Array(4096),
            g = 256,
            h = a.length,
            k = 0,
            l = 1,
            m = 0,
            n = 1;
        c[d++] = a[0];
        for (var r = 1;; r++) {
            n = r + (r >> 1);
            if (n + 1 >= h) break;
            var m = a[n + 1],
                n = a[n],
                p = r & 1 ? m << 4 | n >> 4 : (m & 15) << 8 | n;
            if (p < g)
                if (256 > p) m = d, n = 1, c[d++] = p;
                else
                    for (var m = d, n = f[p], p = e[p], q = p + n; p < q;) c[d++] = c[p++];
            else if (p == g) {
                m = d;
                n = l + 1;
                p = k;
                for (q = k + l; p < q;) c[d++] = c[p++];
                c[d++] = c[k]
            } else break;
            e[g] = k;
            f[g++] = l + 1;
            k = m;
            l = n;
            g = 4096 <= g ? 256 : g
        }
        return d == b ? c : null
    };

    function BigInt(a) {
        this.digits = new Uint16Array(a || 0)
    }
    BigInt.prototype.setBytes = function(a, b) {
        var c = (a.length + 1) / 2 | 0;
        this.digits = new Uint16Array(c);
        if (b)
            for (var d = 0, c = a.length - 1; 0 <= c; c -= 2) this.digits[d++] = a[c] + (0 < c ? 256 * a[c - 1] : 0);
        else
            for (d = 0; d < c; ++d) this.digits[d] = a[2 * d] + 256 * a[2 * d + 1];
        this.trim()
    };
    BigInt.prototype.toInt32 = function() {
        var a = 0;
        0 < this.digits.length && (a = this.digits[0], 1 < this.digits.length && (a |= this.digits[1] << 16));
        return a
    };
    BigInt.prototype.lessThan = function(a) {
        if (this.digits.length == a.digits.length)
            for (var b = this.digits.length - 1; 0 <= b; --b) {
                var c = this.digits[b],
                    d = a.digits[b];
                if (c != d) return c < d
            }
        return this.digits.length < a.digits.length
    };
    BigInt.prototype.shiftRight = function() {
        for (var a = 0, b = this.digits, c = b.length - 1; 0 <= c; --c) {
            var d = b[c];
            b[c] = d >> 1 | a << 15;
            a = d
        }
        this.trim()
    };
    BigInt.prototype.shiftLeft = function(a) {
        if (0 < a) {
            var b = a / 16 | 0;
            a %= 16;
            for (var c = 16 - a, d = this.digits.length + b + 1, e = new BigInt(d), f = 0; f < d; ++f) e.digits[f] = ((f < b || f >= this.digits.length + b ? 0 : this.digits[f - b]) << a | (f < b + 1 ? 0 : this.digits[f - b - 1]) >>> c) & 65535;
            e.trim();
            return e
        }
        return new BigInt(this)
    };
    BigInt.prototype.bitCount = function() {
        var a = 0;
        if (0 < this.digits.length)
            for (var a = 16 * (this.digits.length - 1), b = this.digits[this.digits.length - 1]; b;) b >>>= 1, ++a;
        return a
    };
    BigInt.prototype.sub = function(a) {
        var b = this.digits,
            c = a.digits,
            d = this.digits.length;
        a = a.digits.length;
        for (var e = 0, f = 0; f < d; ++f) {
            var g = b[f],
                h = f < a ? c[f] : 0,
                h = h + e,
                e = h > g ? 1 : 0,
                g = g + (e << 16);
            b[f] = g - h & 65535
        }
        this.trim()
    };
    BigInt.prototype.mul = function(a) {
        for (var b = new BigInt(this.digits.length + a.digits.length), c = b.digits, d = 0; d < this.digits.length; ++d)
            for (var e = this.digits[d], f = 0; f < a.digits.length; ++f)
                for (var g = e * a.digits[f], h = d + f; g;) {
                    var k = (g & 65535) + c[h];
                    c[h] = k & 65535;
                    g >>>= 16;
                    g += k >>> 16;
                    ++h
                }
        b.trim();
        return b
    };
    BigInt.prototype.mod = function(a) {
        if (0 >= this.digits.length || 0 >= a.digits.length) return new BigInt(0);
        var b = new BigInt(this.digits);
        if (!this.lessThan(a)) {
            for (var c = new BigInt(a.digits), c = c.shiftLeft(b.bitCount() - c.bitCount()); !b.lessThan(a);) c.lessThan(b) && b.sub(c), c.shiftRight();
            b.trim()
        }
        return b
    };
    BigInt.prototype.powmod = function(a, b) {
        for (var c = new BigInt([1]), d = this.mod(b); a;) a & 1 && (c = c.mul(d).mod(b)), a >>>= 1, d = d.mul(d).mod(b);
        return c
    };
    BigInt.prototype.trim = function() {
        for (var a = this.digits.length; 0 < a && 0 == this.digits[a - 1];) --a;
        a != this.digits.length && (this.digits = this.digits.subarray(0, a))
    };

    function Bounds(a) {
        for (var b = 0; b < a.length; ++b) {
            var c = a[b].bounds;
            if (void 0 === this.min) this.min = [c.min[0], c.min[1], c.min[2]], this.max = [c.max[0], c.max[1], c.max[2]];
            else
                for (var d = 0; 3 > d; ++d) this.min[d] = Math.min(c.min[d], this.min[d]), this.max[d] = Math.max(c.max[d], this.max[d])
        }
        this.min = this.min ? this.min : [0, 0, 0];
        this.max = this.max ? this.max : [0, 0, 0];
        this.center = [0.5 * (this.min[0] + this.max[0]), 0.5 * (this.min[1] + this.max[1]), 0.5 * (this.min[2] + this.max[2])];
        this.radius = [this.max[0] - this.center[0], this.max[1] - this.center[1],
            this.max[2] - this.center[2]
        ]
    };

    function ByteStream(a) {
        this.bytes = new Uint8Array(a)
    }
    ByteStream.prototype.empty = function() {
        return 0 >= this.bytes.length
    };
    ByteStream.prototype.readCString = function() {
        for (var a = this.bytes, b = a.length, c = 0; c < b; ++c)
            if (0 == a[c]) return a = String.fromCharCode.apply(null, this.bytes.subarray(0, c)), this.bytes = this.bytes.subarray(c + 1), a;
        return null
    };
    ByteStream.prototype.asString = function() {
        for (var a = "", b = 0; b < this.bytes.length; ++b) a += String.fromCharCode(this.bytes[b]);
        return a
    };
    ByteStream.prototype.readBytes = function(a) {
        var b = this.bytes.subarray(0, a);
        this.bytes = this.bytes.subarray(a);
        return b
    };
    ByteStream.prototype.readUint32 = function() {
        var a = this.bytes,
            b = a[0] | a[1] << 8 | a[2] << 16 | a[3] << 24;
        this.bytes = a.subarray(4);
        return b
    };
    var prepareEmbedParams = function(a) {
            a = a || {};
            if (document.location.search)
                for (var b = document.location.search.substring(1).split("&"), c = 0; c < b.length; ++c) {
                    var d = b[c].split("=");
                    a[d[0]] = d[1]
                }
            b = function(a) {
                if (a | 0) return !0;
                for (var b = "true True TRUE yes Yes YES".split(" "), c = 0; c < b.length; ++c)
                    if (a === b[c]) return !0;
                return !1
            };
            a.width = a.width || 800;
            a.height = a.height || 600;
            a.autoStart = b(a.autoStart);
            a.pagePreset = b(a.pagePreset);
            a.fullFrame = b(a.fullFrame) || b(a.bare);
            a.fullFrame = !a.pagePreset && a.fullFrame;
            return a
        },
        embed = function(a, b) {
            var c;
            b = prepareEmbedParams(b);
            var d = b.thumbnailURL;
            if (b.pagePreset) {
                c = new WebViewer(b.width, b.height, a, !!d);
                document.body.style.backgroundColor = "#d7e4da";
                var e = document.createElement("div");
                e.style.position = "relative";
                e.style.backgroundColor = "#e4e7e4";
                e.style.width = b.width + 12 + "px";
                e.style.height = b.height + 6 + 16 + "px";
                e.style.margin = "auto";
                e.style.boxShadow = "3px 5px 12px 0px grey";
                document.body.appendChild(e);
                var f = document.createElement("div");
                f.style.position = "relative";
                f.style.left =
                    "6px";
                f.style.top = "6px";
                e.appendChild(f);
                f.appendChild(c.domRoot);
                if (!c.mobile) {
                    e.style.resize = "both";
                    e.style.overflow = "hidden";
                    var g = [e.style.width, e.style.height],
                        h = function() {
                            if (FullScreen.active()) e.style.resize = "none";
                            else if (e.style.resize = "both", g[0] != e.style.width || g[1] != e.style.height) g[0] = e.style.width, g[1] = e.style.height, c.resize(e.clientWidth - 12, e.clientHeight - 6 - 16);
                            window.setTimeout(h, 100)
                        };
                    h()
                }
            } else c = new WebViewer(b.fullFrame ? window.innerWidth : b.width, b.fullFrame ? window.innerHeight :
                b.height, a, !!d), document.body.appendChild(c.domRoot), b.fullFrame && (c.domRoot.style.position = "absolute", c.domRoot.style.left = c.domRoot.style.top = 0, window.addEventListener("resize", function() {
                FullScreen.active() || c.resize(window.innerWidth, window.innerHeight)
            }));
            c.ui.setThumbnailURL(d);
            b.autoStart && c.loadScene();
            return c
        },
        fetchThumbnail = function(a, b, c, d) {
            var e = -1 == a.indexOf("?") ? "?" : "&";
            Network.fetchBinaryIncremental(a + e + "thumb=1", function(a) {
                (a = (new Archive(a)).extract("thumbnail.jpg")) ? TextureCache.parseFile(a,
                    b, d): c && c();
                return 0
            }, c, 71680)
        },
        marmoset = "undefined" == typeof marmoset ? {} : marmoset;
    marmoset.embed = embed;
    marmoset.fetchThumbnail = fetchThumbnail;

    function Framebuffer(a, b) {
        this.gl = a;
        this.fbo = a.createFramebuffer();
        a.bindFramebuffer(a.FRAMEBUFFER, this.fbo);
        b && (this.width = b.width, this.height = b.height, b.color0 && (this.color0 = b.color0, a.framebufferTexture2D(a.FRAMEBUFFER, a.COLOR_ATTACHMENT0, a.TEXTURE_2D, this.color0.id, 0), this.width = b.color0.desc.width, this.height = b.color0.desc.height), b.depth ? (this.depth = b.depth, a.framebufferTexture2D(a.FRAMEBUFFER, a.DEPTH_ATTACHMENT, a.TEXTURE_2D, this.depth.id, 0)) : (this.depthBuffer = b.depthBuffer, b.createDepth && !this.depthBuffer &&
            (this.depthBuffer = Framebuffer.createDepthBuffer(a, this.width, this.height)), this.depthBuffer && (a.bindRenderbuffer(a.RENDERBUFFER, this.depthBuffer), a.framebufferRenderbuffer(a.FRAMEBUFFER, a.DEPTH_ATTACHMENT, a.RENDERBUFFER, this.depthBuffer), a.bindRenderbuffer(a.RENDERBUFFER, null))));
        this.valid = b && b.ignoreStatus || a.checkFramebufferStatus(a.FRAMEBUFFER) == a.FRAMEBUFFER_COMPLETE;
        a.bindFramebuffer(a.FRAMEBUFFER, null)
    }
    Framebuffer.createDepthBuffer = function(a, b, c) {
        var d = a.createRenderbuffer();
        a.bindRenderbuffer(a.RENDERBUFFER, d);
        a.renderbufferStorage(a.RENDERBUFFER, a.DEPTH_COMPONENT16, b, c);
        a.bindRenderbuffer(a.RENDERBUFFER, null);
        return d
    };
    Framebuffer.prototype.bind = function() {
        this.gl.bindFramebuffer(this.gl.FRAMEBUFFER, this.fbo);
        this.gl.viewport(0, 0, this.width, this.height)
    };
    Framebuffer.bindNone = function(a) {
        a.bindFramebuffer(a.FRAMEBUFFER, null)
    };
    var FullScreen = {
        support: function() {
            return !!(document.fullscreenEnabled || document.webkitFullscreenEnabled || document.mozFullScreenEnabled || document.msFullscreenEnabled)
        },
        begin: function(a, b) {
            var c = a.requestFullscreen || a.webkitRequestFullScreen || a.mozRequestFullScreen || a.msRequestFullscreen;
            if (c) {
                var d = function() {
                    FullScreen.active() || (document.removeEventListener("fullscreenchange", d), document.removeEventListener("webkitfullscreenchange", d), document.removeEventListener("mozfullscreenchange", d), document.removeEventListener("MSFullscreenChange",
                        d));
                    b && b()
                };
                document.addEventListener("fullscreenchange", d);
                document.addEventListener("webkitfullscreenchange", d);
                document.addEventListener("mozfullscreenchange", d);
                document.addEventListener("MSFullscreenChange", d);
                c.bind(a)()
            }
        },
        end: function() {
            var a = document.exitFullscreen || document.webkitExitFullscreen || document.mozCancelFullScreen || document.msExitFullscreen;
            a && a.bind(document)()
        },
        active: function() {
            return !!(document.fullscreenElement || document.webkitIsFullScreen || document.mozFullScreenElement || document.msFullscreenElement)
        }
    };

    function Input(a) {
        this.onTap = [];
        this.onSingleTap = [];
        this.onDoubleTap = [];
        this.onDrag = [];
        this.onZoom = [];
        this.onPan = [];
        this.onPan2 = [];
        this.onAnything = [];
        this.macHax = 0 <= navigator.platform.toUpperCase().indexOf("MAC");
        a && this.attach(a)
    }
    Input.prototype.attach = function(a) {
        this.element = a;
        var b = function(a) {
            for (var b = 0; b < this.onAnything.length; ++b) this.onAnything[b]();
            a.preventDefault()
        }.bind(this);
        this.mouseStates = [{
            pressed: !1,
            position: [0, 0],
            downPosition: [0, 0]
        }, {
            pressed: !1,
            position: [0, 0],
            downPosition: [0, 0]
        }, {
            pressed: !1,
            position: [0, 0],
            downPosition: [0, 0]
        }];
        this.lastTapPos = [0, 0];
        a = function(a) {
            if (a.target === this.element) {
                var d = this.mouseStates[a.button];
                if (d) {
                    d.pressed = !0;
                    var e = this.element.getBoundingClientRect();
                    d.position[0] = d.downPosition[0] =
                        a.clientX - e.left;
                    d.position[1] = d.downPosition[1] = a.clientY - e.top;
                    b(a)
                }
            }
        }.bind(this);
        this.element.addEventListener("mousedown", a);
        a = function(a) {
            var d = this.mouseStates[a.button];
            if (d) {
                var e = this.element.getBoundingClientRect(),
                    f = a.clientX - e.left,
                    e = a.clientY - e.top;
                d.pressed = !1;
                d.position[0] = f;
                d.position[1] = e;
                if (0 == a.button && a.target == this.element && 10 > Math.abs(d.position[0] - d.downPosition[0]) + Math.abs(d.position[1] - d.downPosition[1])) {
                    for (var g = 0; g < this.onTap.length; ++g) this.onTap[g](f, e);
                    this.needSingleClick = !0;
                    window.setTimeout(function(a, b) {
                        if (this.needSingleClick) {
                            for (var c = 0; c < this.onSingleTap.length; ++c) this.onSingleTap[c](a, b);
                            this.needSingleClick = !1
                        }
                    }.bind(this, f, e), 301);
                    d = !1;
                    if (void 0 !== this.doubleClickTimer && (g = 8 > Math.abs(f - this.lastTapPos[0]) + Math.abs(e - this.lastTapPos[1]), 300 > Date.now() - this.doubleClickTimer && g))
                        for (d = !0, this.needSingleClick = !1, g = 0; g < this.onDoubleTap.length; ++g) this.onDoubleTap[g](f, e);
                    this.doubleClickTimer = Date.now();
                    d && (this.doubleClickTimer = -1E9);
                    this.lastTapPos[0] = f;
                    this.lastTapPos[1] =
                        e
                }
            }
            b(a)
        }.bind(this);
        this.element.addEventListener("mouseup", a);
        a = function(a) {
            for (var d = !1, e = 0; 3 > e; ++e) {
                var f = this.mouseStates[e];
                if (f.pressed) {
                    var g = this.element.getBoundingClientRect(),
                        d = a.clientX - g.left,
                        g = a.clientY - g.top,
                        h = d - f.position[0],
                        k = g - f.position[1];
                    f.position[0] = d;
                    f.position[1] = g;
                    if (1 <= e || a.ctrlKey)
                        for (f = 0; f < this.onPan.length; ++f) this.onPan[f](h, k);
                    else if (0 == e)
                        if (a.shiftKey)
                            for (f = 0; f < this.onPan2.length; ++f) this.onPan2[f](h, k);
                        else
                            for (f = 0; f < this.onDrag.length; ++f) this.onDrag[f](d, g, h, k);
                    d = !0
                }
            }
            d && b(a)
        }.bind(this);
        this.element.addEventListener("mousemove", a);
        a = function(a) {
            var d = 0;
            a.deltaY ? (d = -0.4 * a.deltaY, 1 == a.deltaMode ? d *= 16 : 2 == a.deltaMode && (d *= this.element.clientHeight)) : a.wheelDelta ? d = this.macHax && 120 == Math.abs(a.wheelDelta) ? 0.08 * a.wheelDelta : 0.4 * a.wheelDelta : a.detail && (d = -10 * a.detail);
            for (var e = 0; e < this.onZoom.length; ++e) this.onZoom[e](d);
            b(a)
        }.bind(this);
        this.element.addEventListener("mousewheel", a);
        this.element.addEventListener("DOMMouseScroll", a);
        this.element.addEventListener("wheel",
            a);
        a = function(a) {
            for (var b = 0; b < this.mouseStates.length; ++b) this.mouseStates[b].pressed = !1;
            a.preventDefault()
        }.bind(this);
        this.element.addEventListener("mouseleave", a);
        this.element.addEventListener("contextmenu", function(a) {
            a.preventDefault()
        });
        this.touches = {};
        this.tapPossible = !1;
        this.touchCountFloor = 0;
        a = function(a) {
            for (var d = this.element.getBoundingClientRect(), e = !1, f = 0; f < a.changedTouches.length; ++f)
                if (a.target === this.element) {
                    var g = a.changedTouches[f],
                        e = {
                            x: g.clientX - d.left,
                            y: g.clientY - d.top
                        };
                    e.startX =
                        e.x;
                    e.startY = e.y;
                    this.touches[g.identifier] = e;
                    e = !0
                }
            this.tapPossible = 1 == a.touches.length;
            for (g = d = 0; g < this.touches.length; ++g) d++;
            d > this.touchCountFloor && (this.touchCountFloor = d);
            e && b(a)
        }.bind(this);
        this.element.addEventListener("touchstart", a);
        a = function(a) {
            for (var d = !1, e = 0; e < a.changedTouches.length; ++e) {
                var f = a.changedTouches[e],
                    g = this.touches[f.identifier];
                if (g) {
                    if (this.tapPossible) {
                        var h = this.element.getBoundingClientRect(),
                            d = f.clientX - h.left,
                            h = f.clientY - h.top;
                        if (24 > Math.max(Math.abs(d - g.startX),
                                Math.abs(h - g.startY))) {
                            for (e = 0; e < this.onTap.length; ++e) this.onTap[e](d, h);
                            this.needSingleTap = !0;
                            window.setTimeout(function(a, b) {
                                if (this.needSingleTap) {
                                    for (var c = 0; c < this.onSingleTap.length; ++c) this.onSingleTap[c](a, b);
                                    this.needSingleTap = !1
                                }
                            }.bind(this, d, h), 501);
                            g = !1;
                            if (void 0 !== this.doubleTapTimer) {
                                var k = 24 > Math.max(Math.abs(d - this.lastTapPos[0]), Math.abs(h - this.lastTapPos[1])),
                                    l = 500 > Date.now() - this.doubleTapTimer;
                                if (k && l)
                                    for (g = !0, e = 0; e < this.onDoubleTap.length; ++e) this.onDoubleTap[e](d, h)
                            }
                            this.doubleTapTimer =
                                Date.now();
                            g && (this.doubleTapTimer = -1E9);
                            this.lastTapPos[0] = d;
                            this.lastTapPos[1] = h
                        }
                        this.tapPossible = !1
                    }
                    delete this.touches[f.identifier];
                    d = !0
                }
            }
            for (f = e = 0; f < this.touches.length; ++f) e++;
            0 >= e && (this.touchCountFloor = 0);
            d && b(a)
        }.bind(this);
        this.element.addEventListener("touchend", a);
        this.element.addEventListener("touchcancel", a);
        this.element.addEventListener("touchleave", a);
        a = function(a) {
            for (var d = [], e = 0; e < a.touches.length; ++e) a.touches[e].target === this.element && d.push(a.touches[e]);
            var f = this.element.getBoundingClientRect();
            if (1 == d.length && 1 >= this.touchCountFloor) {
                var g = d[0],
                    h = this.touches[g.identifier];
                if (h) {
                    var k = g.clientX - f.left,
                        g = g.clientY - f.top,
                        f = k - h.x,
                        l = g - h.y;
                    h.x = k;
                    h.y = g;
                    for (e = 0; e < this.onDrag.length; ++e) this.onDrag[e](k, g, f, l, a.shiftKey)
                }
            } else if (2 == d.length && 2 >= this.touchCountFloor) {
                if (l = d[0], e = this.touches[l.identifier], g = d[1], h = this.touches[g.identifier], e && h) {
                    var k = l.clientX - f.left,
                        l = l.clientY - f.top,
                        m = g.clientX - f.left,
                        n = g.clientY - f.top,
                        r = Math.sqrt((k - m) * (k - m) + (l - n) * (l - n)),
                        p = Math.sqrt((e.x - h.x) * (e.x - h.x) + (e.y -
                            h.y) * (e.y - h.y)),
                        q = Math.abs(r - p),
                        f = (k - e.x + m - h.x) / 2,
                        g = (l - e.y + n - h.y) / 2,
                        u = Math.sqrt(f * f + g * g);
                    e.x = k;
                    e.y = l;
                    h.x = m;
                    h.y = n;
                    if (0 < q)
                        for (h = q / (q + u), e = 0; e < this.onZoom.length; ++e) this.onZoom[e](2 * (r - p) * h);
                    if (0 < u)
                        for (h = u / (q + u), e = 0; e < this.onDrag.length; ++e) this.onPan[e](f * h, g * h)
                }
            } else if (3 <= d.length) {
                for (e = p = r = m = l = 0; e < d.length; ++e) g = d[e], h = this.touches[g.identifier], k = g.clientX - f.left, g = g.clientY - f.top, r += k, p += g, h && (l += h.x, m += h.y, h.x = k, h.y = g);
                l /= d.length;
                m /= d.length;
                r /= d.length;
                p /= d.length;
                for (e = 0; e < this.onPan2.length; ++e) this.onPan2[e](r -
                    l, p - m)
            }
            0 < d.length && b(a)
        }.bind(this);
        this.element.addEventListener("touchmove", a)
    };

    function Lights(a, b) {
        this.rotation = this.shadowCount = this.count = 0;
        this.positions = [];
        this.directions = [];
        this.matrixWeights = [];
        this.matrix = Matrix.identity();
        this.invMatrix = Matrix.identity();
        for (var c in a) this[c] = a[c];
        this.count = this.positions.length / 4;
        this.count = Math.min(6, this.count);
        this.shadowCount = Math.min(3, this.shadowCount);
        this.positions = new Float32Array(this.positions);
        this.positionBuffer = new Float32Array(this.positions);
        this.directions = new Float32Array(this.directions);
        this.directionBuffer =
            new Float32Array(this.directions);
        this.modelViewBuffer = new Float32Array(16 * this.shadowCount);
        this.projectionBuffer = new Float32Array(16 * this.shadowCount);
        this.finalTransformBuffer = new Float32Array(16 * this.shadowCount);
        this.shadowTexelPadProjections = new Float32Array(4 * this.shadowCount);
        this.shadowsNeedUpdate = new Uint8Array(this.shadowCount);
        for (var d = 0; d < this.shadowsNeedUpdate.length; ++d) this.shadowsNeedUpdate[d] = 1;
        Matrix.rotation(this.matrix, this.rotation, 1);
        Matrix.transpose(this.invMatrix, this.matrix);
        for (d = 0; d < this.count; ++d) {
            c = this.positions.subarray(4 * d, 4 * d + 4);
            var e = this.directions.subarray(3 * d, 3 * d + 3);
            1 == this.matrixWeights[d] ? (Matrix.mul4(c, this.matrix, c[0], c[1], c[2], c[3]), Matrix.mulVec(e, this.matrix, e[0], e[1], e[2])) : 2 == this.matrixWeights[d] && (Matrix.mul4(c, b.viewMatrix, c[0], c[1], c[2], c[3]), Matrix.mulVec(e, b.viewMatrix, e[0], e[1], e[2]))
        }
    }
    Lights.prototype.getLightPos = function(a) {
        return this.positionBuffer.subarray(4 * a, 4 * a + 4)
    };
    Lights.prototype.getLightDir = function(a) {
        return this.directionBuffer.subarray(3 * a, 3 * a + 3)
    };
    Lights.prototype.update = function(a, b) {
        var c = new Matrix.type(this.matrix);
        Matrix.rotation(this.matrix, this.rotation, 1);
        Matrix.transpose(this.invMatrix, this.matrix);
        for (var d = 0; d < this.count; ++d) {
            var e = this.positions.subarray(4 * d, 4 * d + 4),
                f = this.directions.subarray(3 * d, 3 * d + 3),
                g = this.getLightPos(d),
                h = this.getLightDir(d);
            1 == this.matrixWeights[d] ? (g[0] = e[0], g[1] = e[1], g[2] = e[2], g[3] = e[3], h[0] = f[0], h[1] = f[1], h[2] = f[2]) : 2 == this.matrixWeights[d] ? (Matrix.mul4(g, a.transform, e[0], e[1], e[2], e[3]), Matrix.mulVec(h,
                a.transform, f[0], f[1], f[2]), Matrix.mul4(g, this.matrix, g[0], g[1], g[2], g[3]), Matrix.mulVec(h, this.matrix, h[0], h[1], h[2])) : (Matrix.mul4(g, this.matrix, e[0], e[1], e[2], e[3]), Matrix.mulVec(h, this.matrix, f[0], f[1], f[2]));
            Vect.normalize(h, h)
        }
        for (var f = new Float32Array(this.finalTransformBuffer), g = Matrix.empty(), h = Matrix.empty(), k = Matrix.empty(), l = Vect.empty(), m = Vect.empty(), n = Vect.empty(), r = Vect.empty(), e = Vect.empty(), p = [], q = [], u = Matrix.create(0.5, 0, 0, 0.5, 0, 0.5, 0, 0.5, 0, 0, 0.5, 0.5, 0, 0, 0, 1), d = 0; d < this.count; ++d) {
            l =
                this.getLightPos(d);
            m = this.getLightDir(d);
            0.99 < Math.abs(m[1]) ? Vect.set(n, 1, 0, 0) : Vect.set(n, 0, 1, 0);
            Vect.cross(r, n, m);
            Vect.normalize(r, r);
            Vect.cross(n, m, r);
            Vect.normalize(n, n);
            Matrix.set(g, r[0], r[1], r[2], -Vect.dot(r, l), n[0], n[1], n[2], -Vect.dot(n, l), m[0], m[1], m[2], -Vect.dot(m, l), 0, 0, 0, 1);
            for (l = 0; 8 > l; ++l) e[0] = l & 1 ? b.max[0] : b.min[0], e[1] = l & 2 ? b.max[1] : b.min[1], e[2] = l & 4 ? b.max[2] : b.min[2], Matrix.mulPoint(e, this.matrix, 1.005 * e[0], 1.005 * e[1], 1.005 * e[2]), Matrix.mulPoint(e, g, e[0], e[1], e[2]), 0 == l ? (p[0] = q[0] = e[0],
                p[1] = q[1] = e[1], p[2] = q[2] = e[2]) : (p[0] = Math.min(p[0], e[0]), p[1] = Math.min(p[1], e[1]), p[2] = Math.min(p[2], e[2]), q[0] = Math.max(q[0], e[0]), q[1] = Math.max(q[1], e[1]), q[2] = Math.max(q[2], e[2]));
            var l = -p[2],
                m = -q[2],
                s = this.spot[3 * d];
            0 < s ? (l = Math.min(l, 1 / this.parameters[3 * d + 2]), m = Math.max(0.005 * l, m), Matrix.perspective(h, s, 1, m, l), d < this.shadowCount && (l = 2 * -Math.tan(0.00872664625 * s), this.shadowTexelPadProjections[4 * d + 0] = this.modelViewBuffer[16 * d + 2] * l, this.shadowTexelPadProjections[4 * d + 1] = this.modelViewBuffer[16 * d +
                6] * l, this.shadowTexelPadProjections[4 * d + 2] = this.modelViewBuffer[16 * d + 10] * l, this.shadowTexelPadProjections[4 * d + 3] = this.modelViewBuffer[16 * d + 14] * l)) : (Matrix.ortho(h, p[0], q[0], p[1], q[1], m, l), d < this.shadowCount && (this.shadowTexelPadProjections[4 * d + 0] = this.shadowTexelPadProjections[4 * d + 1] = this.shadowTexelPadProjections[4 * d + 2] = 0, this.shadowTexelPadProjections[4 * d + 3] = Math.max(q[0] - p[0], q[1] - p[1])));
            Matrix.mul(k, h, g);
            Matrix.mul(k, u, k);
            Matrix.copyToBuffer(this.modelViewBuffer, 16 * d, g);
            Matrix.copyToBuffer(this.projectionBuffer,
                16 * d, h);
            Matrix.copyToBuffer(this.finalTransformBuffer, 16 * d, k)
        }
        e = !1;
        for (d = 0; d < c.length; ++d)
            if (c[d] != this.matrix[d]) {
                e = !0;
                break
            }
        for (d = 0; d < this.shadowCount; d++)
            if (e && 1 == this.matrixWeights[d]) this.shadowsNeedUpdate[d] = 1;
            else
                for (c = 16 * d; c < 16 * d + 16; ++c)
                    if (f[c] != this.finalTransformBuffer[c]) {
                        this.shadowsNeedUpdate[d] = 1;
                        break
                    }
    };

    function Material(a, b, c) {
        this.gl = a;
        this.name = c.name;
        var d = {
                mipmap: !0,
                aniso: a.hints.mobile ? 0 : 4,
                clamp: !!c.textureWrapClamp,
                mirror: !!c.textureWrapMirror
            },
            e = {
                mipmap: d.mipmap,
                clamp: d.clamp,
                mirror: d.mirror,
                nofilter: c.textureFilterNearest || !1
            };
        e.nofilter || (e.aniso = a.hints.mobile ? 2 : 4);
        this.textures = {
            albedo: a.textureCache.fromFilesMergeAlpha(b.get(c.albedoTex), b.get(c.alphaTex), e),
            reflectivity: a.textureCache.fromFilesMergeAlpha(b.get(c.reflectivityTex), b.get(c.glossTex), d),
            normal: a.textureCache.fromFile(b.get(c.normalTex),
                d),
            extras: a.textureCache.fromFilesMergeAlpha(b.get(c.extrasTex), b.get(c.extrasTexA), d)
        };
        this.extrasTexCoordRanges = {};
        if (c.extrasTexCoordRanges)
            for (var f in c.extrasTexCoordRanges) this.extrasTexCoordRanges[f] = new Float32Array(c.extrasTexCoordRanges[f].scaleBias);
        this.textures.extras || (b = new Texture(a, {
            width: 1,
            height: 1
        }), b.loadArray(new Uint8Array([255, 255, 255, 255])), this.textures.extras = b);
        var g = c.blendTint || [1, 1, 1];
        b = {
            none: function() {
                a.disable(a.BLEND)
            },
            alpha: function() {
                a.enable(a.BLEND);
                a.blendFunc(a.SRC_ALPHA,
                    a.ONE_MINUS_SRC_ALPHA)
            },
            add: function() {
                a.enable(a.BLEND);
                a.blendColor(g[0], g[1], g[2], 1);
                a.blendFunc(a.ONE, a.CONSTANT_COLOR)
            }
        };
        this.blend = b[c.blend] || b.none;
        this.alphaTest = c.alphaTest || 0;
        this.usesBlending = this.blend !== b.none;
        this.shadowAlphaTest = this.alphaTest;
        0 >= this.shadowAlphaTest && this.blend === b.alpha && (this.shadowAlphaTest = 0.5);
        this.castShadows = this.blend !== b.add;
        this.horizonOcclude = c.horizonOcclude || 0;
        this.fresnel = new Float32Array(c.fresnel ? c.fresnel : [1, 1, 1]);
        this.emissiveIntensity = c.emissiveIntensity ||
            1;
        d = !1;
        e = [];
        0 < c.lightCount && e.push("#define LIGHT_COUNT " + c.lightCount);
        0 < c.shadowCount && e.push("#define SHADOW_COUNT " + Math.min(c.lightCount, c.shadowCount));
        0 < c.alphaTest && e.push("#define ALPHA_TEST");
        this.blend === b.alpha && e.push("#define TRANSPARENCY_DITHER");
        a.hints.mobile && e.push("#define MOBILE");
        c.useSkin && (e.push("#define SKIN"), this.skinParams = c.skinParams || {
            subdermisColor: [1, 1, 1],
            transColor: [1, 0, 0, 0.5],
            fresnelColor: [0.2, 0.2, 0.2, 0.5],
            fresnelOcc: 1,
            fresnelGlossMask: 1,
            transSky: 0.5,
            shadowBlur: 0.5,
            normalSmooth: 0.5
        }, this.skinParams.fresnelIntegral = 1 / 3.14159 * (1 - 0.5 * this.skinParams.fresnelColor[3]), this.skinParams.transIntegral = 1 / 3.14159 * (1 - 0.5 * this.skinParams.transColor[3]), this.skinParams.transSky *= 1.25, this.skinParams.transIntegral *= 1.25, this.extrasTexCoordRanges.subdermisTex || e.push("#define SKIN_NO_SUBDERMIS_TEX"), this.extrasTexCoordRanges.translucencyTex || e.push("#define SKIN_NO_TRANSLUCENCY_TEX"), this.extrasTexCoordRanges.fuzzTex || e.push("#define SKIN_NO_FUZZ_TEX"));
        c.aniso && (e.push("#define ANISO"),
            this.anisoParams = c.anisoParams || {
                strength: 1,
                tangent: [1, 0, 0],
                integral: 0.5
            }, this.extrasTexCoordRanges.anisoTex || e.push("#define ANISO_NO_DIR_TEX"));
        c.microfiber && (e.push("#define MICROFIBER"), this.microfiberParams = c.microfiberParams || {
            fresnelColor: [0.2, 0.2, 0.2, 0.5],
            fresnelOcc: 1,
            fresnelGlossMask: 1
        }, this.microfiberParams.fresnelIntegral = 1 / 3.14159 * (1 - 0.5 * this.microfiberParams.fresnelColor[3]), this.extrasTexCoordRanges.fuzzTex || e.push("#define MICROFIBER_NO_FUZZ_TEX"));
        c.vertexColor && (e.push("#define VERTEX_COLOR"),
            c.vertexColorsRGB && e.push("#define VERTEX_COLOR_SRGB"), c.vertexColorAlpha && e.push("#define VERTEX_COLOR_ALPHA"));
        this.horizonSmoothing = c.horizonSmoothing || 0;
        0 < this.horizonSmoothing && e.push("#define HORIZON_SMOOTHING");
        c.unlitDiffuse && e.push("#define DIFFUSE_UNLIT");
        this.extrasTexCoordRanges.emissiveTex && (e.push("#define EMISSIVE"), c.emissiveSecondaryUV && (e.push("#define EMISSIVE_SECONDARY_UV"), d = !0));
        this.extrasTexCoordRanges.aoTex && (e.push("#define AMBIENT_OCCLUSION"), c.aoSecondaryUV && (e.push("#define AMBIENT_OCCLUSION_SECONDARY_UV"),
            d = !0));
        c.tangentOrthogonalize && e.push("#define TSPACE_ORTHOGONALIZE");
        c.tangentNormalize && e.push("#define TSPACE_RENORMALIZE");
        c.tangentGenerateBitangent && e.push("#define TSPACE_COMPUTE_BITANGENT");
        d && e.push("#define TEXCOORD_SECONDARY");
        this.shader = a.shaderCache.fromURLs("matvert.glsl", "matfrag.glsl", e);
        e.push("#define STRIPVIEW");
        this.stripShader = a.shaderCache.fromURLs("matvert.glsl", "matfrag.glsl", e);
        this.wireShader = a.shaderCache.fromURLs("wirevert.glsl", "wirefrag.glsl");
        this.blend === b.alpha &&
            (this.prepassShader = a.shaderCache.fromURLs("alphaprepassvert.glsl", "alphaprepassfrag.glsl"))
    }
    Material.prototype.bind = function(a) {
        if (!this.complete()) return !1;
        var b = a.view,
            c = a.lights,
            d = a.sky,
            e = a.shadow,
            f = a.stripData.active() ? this.stripShader : this.shader,
            g = this.skinParams,
            h = this.anisoParams,
            k = this.microfiberParams,
            l, m = this.gl,
            n = f.params,
            r = this.textures,
            p = f.samplers;
        f.bind();
        this.blend();
        var q = Matrix.mul(Matrix.empty(), b.projectionMatrix, b.viewMatrix);
        m.uniformMatrix4fv(n.uModelViewProjectionMatrix, !1, q);
        m.uniformMatrix4fv(n.uSkyMatrix, !1, c.matrix);
        q = Matrix.mulPoint(Vect.empty(), c.matrix, b.transform[12],
            b.transform[13], b.transform[14]);
        m.uniform3f(n.uCameraPosition, q[0], q[1], q[2]);
        m.uniform3fv(n.uFresnel, this.fresnel);
        m.uniform1f(n.uAlphaTest, this.alphaTest);
        m.uniform1f(n.uHorizonOcclude, this.horizonOcclude);
        m.uniform1f(n.uHorizonSmoothing, this.horizonSmoothing);
        m.uniform4fv(n.uDiffuseCoefficients, d.diffuseCoefficients);
        if (0 < c.count && (m.uniform4fv(n.uLightPositions, c.positionBuffer), m.uniform3fv(n.uLightDirections, c.directionBuffer), m.uniform3fv(n.uLightColors, c.colors), m.uniform3fv(n.uLightParams,
                c.parameters), m.uniform3fv(n.uLightSpot, c.spot), q = 0.392699 * a.postRender.sampleIndex, m.uniform2f(n.uShadowKernelRotation, 0.5 * Math.cos(q), 0.5 * Math.sin(q)), 0 < c.shadowCount)) {
            var q = e.depthTextures[0].desc.width,
                u = e.depthTextures[0].desc.height;
            m.uniform4f(n.uShadowMapSize, q, u, 1 / q, 1 / u);
            m.uniformMatrix4fv(n.uShadowMatrices, !1, c.finalTransformBuffer);
            m.uniform4fv(n.uShadowTexelPadProjections, c.shadowTexelPadProjections);
            e.bindDepthTexture(p.tDepth0, 0);
            e.bindDepthTexture(p.tDepth1, 1);
            e.bindDepthTexture(p.tDepth2,
                2)
        }
        g && (m.uniform3fv(n.uSubdermisColor, g.subdermisColor), m.uniform4fv(n.uTransColor, g.transColor), m.uniform4fv(n.uFresnelColor, g.fresnelColor), m.uniform1f(n.uFresnelOcc, g.fresnelOcc), m.uniform1f(n.uFresnelGlossMask, g.fresnelGlossMask), m.uniform1f(n.uFresnelIntegral, g.fresnelIntegral), m.uniform1f(n.uTransIntegral, g.transIntegral), m.uniform1f(n.uTransSky, g.transSky), m.uniform1f(n.uSkinShadowBlur, 8 * Math.min(g.shadowBlur, 1)), m.uniform1f(n.uNormalSmooth, g.normalSmooth), (l = this.extrasTexCoordRanges.subdermisTex) &&
            m.uniform4fv(n.uTexRangeSubdermis, l), (l = this.extrasTexCoordRanges.translucencyTex) && m.uniform4fv(n.uTexRangeTranslucency, l), (l = this.extrasTexCoordRanges.fuzzTex) && m.uniform4fv(n.uTexRangeFuzz, l));
        k && (m.uniform4fv(n.uFresnelColor, k.fresnelColor), m.uniform1f(n.uFresnelOcc, k.fresnelOcc), m.uniform1f(n.uFresnelGlossMask, k.fresnelGlossMask), m.uniform1f(n.uFresnelIntegral, k.fresnelIntegral), (l = this.extrasTexCoordRanges.fuzzTex) && m.uniform4fv(n.uTexRangeFuzz, l));
        h && (m.uniform3fv(n.uAnisoTangent, h.tangent),
            m.uniform1f(n.uAnisoStrength, h.strength), m.uniform1f(n.uAnisoIntegral, h.integral), (l = this.extrasTexCoordRanges.anisoTex) && m.uniform4fv(n.uTexRangeAniso, l));
        if (l = this.extrasTexCoordRanges.emissiveTex) m.uniform4fv(n.uTexRangeEmissive, l), m.uniform1f(n.uEmissiveScale, this.emissiveIntensity);
        (l = this.extrasTexCoordRanges.aoTex) && m.uniform4fv(n.uTexRangeAO, l);
        r.albedo.bind(p.tAlbedo);
        r.reflectivity.bind(p.tReflectivity);
        r.normal.bind(p.tNormal);
        r.extras.bind(p.tExtras);
        d.specularTexture.bind(p.tSkySpecular);
        f === this.stripShader && (m.uniform1fv(n.uStrips, a.stripData.strips), m.uniform2f(n.uStripRes, 2 / b.size[0], 2 / b.size[1]));
        return !0
    };
    Material.prototype.bindAlphaPrepass = function(a) {
        if (!this.complete() || !this.prepassShader) return !1;
        var b = this.gl,
            c = this.prepassShader.params,
            d = this.prepassShader.samplers;
        this.prepassShader.bind();
        a = Matrix.mul(Matrix.empty(), a.view.projectionMatrix, a.view.viewMatrix);
        b.uniformMatrix4fv(c.uModelViewProjectionMatrix, !1, a);
        this.textures.albedo.bind(d.tAlbedo);
        return !0
    };
    Material.prototype.bindWire = function(a) {
        if (!this.complete()) return !1;
        var b = this.gl,
            c = this.wireShader.params,
            d = a.view;
        b.enable(b.BLEND);
        b.blendFunc(b.SRC_ALPHA, b.ONE_MINUS_SRC_ALPHA);
        b.depthMask(!1);
        this.wireShader.bind();
        var e = Matrix.mul(Matrix.empty(), d.projectionMatrix, d.viewMatrix);
        b.uniformMatrix4fv(c.uModelViewProjectionMatrix, !1, e);
        b.uniform4f(c.uStripParams, 2 / d.size[0], 2 / d.size[1], a.stripData.strips[3], a.stripData.strips[4]);
        return !0
    };
    Material.prototype.complete = function() {
        return this.wireShader.complete() && this.shader.complete() && this.stripShader.complete() && (!this.prepassShader || this.prepassShader.complete()) && this.textures.albedo.complete() && this.textures.reflectivity.complete() && this.textures.normal.complete()
    };
    var Matrix = {
        type: Float32Array,
        create: function(a, b, c, d, e, f, g, h, k, l, m, n, r, p, q, u) {
            var s = new Matrix.type(16);
            s[0] = a;
            s[4] = b;
            s[8] = c;
            s[12] = d;
            s[1] = e;
            s[5] = f;
            s[9] = g;
            s[13] = h;
            s[2] = k;
            s[6] = l;
            s[10] = m;
            s[14] = n;
            s[3] = r;
            s[7] = p;
            s[11] = q;
            s[15] = u;
            return s
        },
        empty: function() {
            return new Matrix.type(16)
        },
        identity: function() {
            var a = new Matrix.type(16);
            a[0] = 1;
            a[4] = 0;
            a[8] = 0;
            a[12] = 0;
            a[1] = 0;
            a[5] = 1;
            a[9] = 0;
            a[13] = 0;
            a[2] = 0;
            a[6] = 0;
            a[10] = 1;
            a[14] = 0;
            a[3] = 0;
            a[7] = 0;
            a[11] = 0;
            a[15] = 1;
            return a
        },
        set: function(a, b, c, d, e, f, g, h, k, l, m, n, r, p, q, u, s) {
            a[0] =
                b;
            a[4] = c;
            a[8] = d;
            a[12] = e;
            a[1] = f;
            a[5] = g;
            a[9] = h;
            a[13] = k;
            a[2] = l;
            a[6] = m;
            a[10] = n;
            a[14] = r;
            a[3] = p;
            a[7] = q;
            a[11] = u;
            a[15] = s
        },
        translation: function(a, b, c, d) {
            Matrix.set(a, 1, 0, 0, b, 0, 1, 0, c, 0, 0, 1, d, 0, 0, 0, 1);
            return a
        },
        rotation: function(a, b, c) {
            a[0] = 1;
            a[4] = 0;
            a[8] = 0;
            a[12] = 0;
            a[1] = 0;
            a[5] = 1;
            a[9] = 0;
            a[13] = 0;
            a[2] = 0;
            a[6] = 0;
            a[10] = 1;
            a[14] = 0;
            a[3] = 0;
            a[7] = 0;
            a[11] = 0;
            a[15] = 1;
            var d = 0.0174532925 * b;
            b = Math.sin(d);
            d = Math.cos(d);
            switch (c) {
                case 0:
                    a[5] = d;
                    a[9] = -b;
                    a[6] = b;
                    a[10] = d;
                    break;
                case 1:
                    a[0] = d;
                    a[8] = b;
                    a[2] = -b;
                    a[10] = d;
                    break;
                case 2:
                    a[0] = d,
                        a[4] = -b, a[1] = b, a[5] = d
            }
            return a
        },
        mul: function(a, b, c) {
            var d = b[0],
                e = b[1],
                f = b[2],
                g = b[3],
                h = b[4],
                k = b[5],
                l = b[6],
                m = b[7],
                n = b[8],
                r = b[9],
                p = b[10],
                q = b[11],
                u = b[12],
                s = b[13],
                z = b[14];
            b = b[15];
            var t = c[0],
                v = c[1],
                w = c[2],
                x = c[3];
            a[0] = t * d + v * h + w * n + x * u;
            a[1] = t * e + v * k + w * r + x * s;
            a[2] = t * f + v * l + w * p + x * z;
            a[3] = t * g + v * m + w * q + x * b;
            t = c[4];
            v = c[5];
            w = c[6];
            x = c[7];
            a[4] = t * d + v * h + w * n + x * u;
            a[5] = t * e + v * k + w * r + x * s;
            a[6] = t * f + v * l + w * p + x * z;
            a[7] = t * g + v * m + w * q + x * b;
            t = c[8];
            v = c[9];
            w = c[10];
            x = c[11];
            a[8] = t * d + v * h + w * n + x * u;
            a[9] = t * e + v * k + w * r + x * s;
            a[10] = t * f + v * l + w * p + x * z;
            a[11] =
                t * g + v * m + w * q + x * b;
            t = c[12];
            v = c[13];
            w = c[14];
            x = c[15];
            a[12] = t * d + v * h + w * n + x * u;
            a[13] = t * e + v * k + w * r + x * s;
            a[14] = t * f + v * l + w * p + x * z;
            a[15] = t * g + v * m + w * q + x * b;
            return a
        },
        invert: function(a, b) {
            var c = b[0],
                d = b[1],
                e = b[2],
                f = b[3],
                g = b[4],
                h = b[5],
                k = b[6],
                l = b[7],
                m = b[8],
                n = b[9],
                r = b[10],
                p = b[11],
                q = b[12],
                u = b[13],
                s = b[14],
                z = b[15],
                t = c * h - d * g,
                v = c * k - e * g,
                w = c * l - f * g,
                x = d * k - e * h,
                A = d * l - f * h,
                B = e * l - f * k,
                C = m * u - n * q,
                D = m * s - r * q,
                E = m * z - p * q,
                F = n * s - r * u,
                G = n * z - p * u,
                H = r * z - p * s,
                y = t * H - v * G + w * F + x * E - A * D + B * C;
            if (!y) return null;
            y = 1 / y;
            a[0] = (h * H - k * G + l * F) * y;
            a[1] = (e * G - d * H - f * F) * y;
            a[2] = (u * B - s * A + z * x) * y;
            a[3] = (r * A - n * B - p * x) * y;
            a[4] = (k * E - g * H - l * D) * y;
            a[5] = (c * H - e * E + f * D) * y;
            a[6] = (s * w - q * B - z * v) * y;
            a[7] = (m * B - r * w + p * v) * y;
            a[8] = (g * G - h * E + l * C) * y;
            a[9] = (d * E - c * G - f * C) * y;
            a[10] = (q * A - u * w + z * t) * y;
            a[11] = (n * w - m * A - p * t) * y;
            a[12] = (h * D - g * F - k * C) * y;
            a[13] = (c * F - d * D + e * C) * y;
            a[14] = (u * v - q * x - s * t) * y;
            a[15] = (m * x - n * v + r * t) * y;
            return a
        },
        transpose: function(a, b) {
            a[0] = b[0];
            a[4] = b[1];
            a[8] = b[2];
            a[12] = b[3];
            a[1] = b[4];
            a[5] = b[5];
            a[9] = b[6];
            a[13] = b[7];
            a[2] = b[8];
            a[6] = b[9];
            a[10] = b[10];
            a[14] = b[11];
            a[3] = b[12];
            a[7] = b[13];
            a[11] = b[14];
            a[15] = b[15];
            return a
        },
        mul4: function(a, b, c, d, e, f) {
            a[0] = b[0] * c + b[4] * d + b[8] * e + b[12] * f;
            a[1] = b[1] * c + b[5] * d + b[9] * e + b[13] * f;
            a[2] = b[2] * c + b[6] * d + b[10] * e + b[14] * f;
            a[3] = b[3] * c + b[7] * d + b[11] * e + b[15] * f;
            return a
        },
        mulPoint: function(a, b, c, d, e) {
            a[0] = b[0] * c + b[4] * d + b[8] * e + b[12];
            a[1] = b[1] * c + b[5] * d + b[9] * e + b[13];
            a[2] = b[2] * c + b[6] * d + b[10] * e + b[14];
            return a
        },
        mulVec: function(a, b, c, d, e) {
            a[0] = b[0] * c + b[4] * d + b[8] * e;
            a[1] = b[1] * c + b[5] * d + b[9] * e;
            a[2] = b[2] * c + b[6] * d + b[10] * e;
            return a
        },
        perspective: function(a, b, c, d, e, f) {
            f = f || 0;
            b = 1 / Math.tan(0.00872664625 *
                b);
            a[0] = b / c;
            a[1] = a[2] = a[3] = 0;
            a[5] = b;
            a[4] = a[6] = a[7] = 0;
            a[8] = a[9] = 0;
            a[10] = (e + d) / (d - e) - 3.0518044E-5 * f;
            a[11] = -1;
            a[14] = 2 * e * d / (d - e);
            a[12] = a[13] = a[15] = 0;
            return a
        },
        perspectiveInfinite: function(a, b, c, d, e) {
            e = e || 0;
            b = 1 / Math.tan(0.00872664625 * b);
            a[0] = b / c;
            a[1] = a[2] = a[3] = 0;
            a[5] = b;
            a[4] = a[6] = a[7] = 0;
            a[8] = a[9] = 0;
            a[10] = a[11] = -1 - 3.0518044E-5 * e;
            a[14] = -2 * d;
            a[12] = a[13] = a[15] = 0;
            return a
        },
        ortho: function(a, b, c, d, e, f, g, h) {
            var k = 1 / (c - b),
                l = 1 / (e - d),
                m = 1 / (g - f);
            a[0] = k + k;
            a[1] = a[2] = a[3] = 0;
            a[5] = l + l;
            a[4] = a[6] = a[7] = 0;
            a[12] = -(c + b) * k;
            a[13] = -(e + d) * l;
            a[10] = -(m + m) - 3.0518044E-5 * (h || 0);
            a[14] = -(g + f) * m;
            a[8] = a[9] = a[11] = 0;
            a[15] = 1;
            return a
        },
        lookAt: function(a, b, c, d) {
            var e = a.subarray(0, 3),
                f = a.subarray(4, 7),
                g = a.subarray(8, 11);
            Vect.sub(g, b, c);
            Vect.cross(e, d, g);
            Vect.normalize(g, g);
            Vect.normalize(e, e);
            Vect.cross(f, g, e);
            Matrix.set(a, e[0], e[1], e[2], -Vect.dot(e, b), f[0], f[1], f[2], -Vect.dot(f, b), g[0], g[1], g[2], -Vect.dot(g, b), 0, 0, 0, 1)
        },
        copy: function(a, b) {
            for (var c = 0; 16 > c; ++c) a[c] = b[c]
        },
        copyToBuffer: function(a, b, c) {
            for (var d = 0; 16 > d; ++d) a[b + d] = c[d]
        }
    };

    function Mesh(a, b, c) {
        this.gl = a;
        this.desc = b;
        this.name = b.name;
        this.modelMatrix = Matrix.identity();
        this.origin = b.transform ? Vect.create(b.transform[12], b.transform[13], b.transform[14], 1) : Vect.create(0, 5, 0, 1);
        this.stride = 32;
        if (this.vertexColor = b.vertexColor) this.stride += 4;
        if (this.secondaryTexCoord = b.secondaryTexCoord) this.stride += 8;
        c = new ByteStream(c.data);
        this.indexCount = b.indexCount;
        this.indexTypeSize = b.indexTypeSize;
        this.indexType = 4 == this.indexTypeSize ? a.UNSIGNED_INT : a.UNSIGNED_SHORT;
        this.indexBuffer =
            a.createBuffer();
        a.bindBuffer(a.ELEMENT_ARRAY_BUFFER, this.indexBuffer);
        var d = c.readBytes(this.indexCount * this.indexTypeSize);
        a.bufferData(a.ELEMENT_ARRAY_BUFFER, d, a.STATIC_DRAW);
        this.wireCount = b.wireCount;
        this.wireBuffer = a.createBuffer();
        a.bindBuffer(a.ELEMENT_ARRAY_BUFFER, this.wireBuffer);
        d = c.readBytes(this.wireCount * this.indexTypeSize);
        a.bufferData(a.ELEMENT_ARRAY_BUFFER, d, a.STATIC_DRAW);
        a.bindBuffer(a.ELEMENT_ARRAY_BUFFER, null);
        this.vertexCount = b.vertexCount;
        this.vertexBuffer = a.createBuffer();
        a.bindBuffer(a.ARRAY_BUFFER, this.vertexBuffer);
        c = c.readBytes(this.vertexCount * this.stride);
        a.bufferData(a.ARRAY_BUFFER, c, a.STATIC_DRAW);
        a.bindBuffer(a.ARRAY_BUFFER, null);
        this.bounds = void 0 === b.minBound || void 0 === b.maxBound ? {
            min: Vect.create(-10, -10, -10, 1),
            max: Vect.create(10, 10, -0, 1)
        } : {
            min: Vect.create(b.minBound[0], b.minBound[1], b.minBound[2], 1),
            max: Vect.create(b.maxBound[0], b.maxBound[1], b.maxBound[2], 1)
        };
        this.bounds.maxExtent = Math.max(Math.max(b.maxBound[0] - b.minBound[0], b.maxBound[1] - b.minBound[1]),
            b.maxBound[2] - b.minBound[2])
    };

    function MeshRenderable(a, b, c) {
        this.mesh = a;
        this.gl = this.mesh.gl;
        this.indexOffset = b.firstIndex * a.indexTypeSize;
        this.indexCount = b.indexCount;
        this.wireIndexOffset = b.firstWireIndex * a.indexTypeSize;
        this.wireIndexCount = b.wireIndexCount;
        this.material = c
    }
    MeshRenderable.prototype.draw = function(a) {
        var b = this.gl;
        if (this.material.bind(a)) {
            a = this.material.shader.attribs;
            var c = this.mesh.stride;
            this.mesh.desc.cullBackFaces ? (b.enable(b.CULL_FACE), b.cullFace(b.BACK)) : b.disable(b.CULL_FACE);
            b.bindBuffer(b.ELEMENT_ARRAY_BUFFER, this.mesh.indexBuffer);
            b.bindBuffer(b.ARRAY_BUFFER, this.mesh.vertexBuffer);
            b.enableVertexAttribArray(a.vPosition);
            b.enableVertexAttribArray(a.vTexCoord);
            b.enableVertexAttribArray(a.vTangent);
            b.enableVertexAttribArray(a.vBitangent);
            b.enableVertexAttribArray(a.vNormal);
            var d = this.mesh.vertexColor && void 0 !== a.vColor;
            d && b.enableVertexAttribArray(a.vColor);
            var e = this.mesh.secondaryTexCoord && void 0 !== a.vTexCoord2;
            e && b.enableVertexAttribArray(a.vTexCoord2);
            var f = 0;
            b.vertexAttribPointer(a.vPosition, 3, b.FLOAT, !1, c, f);
            f += 12;
            b.vertexAttribPointer(a.vTexCoord, 2, b.FLOAT, !1, c, f);
            f += 8;
            this.mesh.secondaryTexCoord && (e && b.vertexAttribPointer(a.vTexCoord2, 2, b.FLOAT, !1, c, f), f += 8);
            b.vertexAttribPointer(a.vTangent, 2, b.UNSIGNED_SHORT, !0, c, f);
            f += 4;
            b.vertexAttribPointer(a.vBitangent,
                2, b.UNSIGNED_SHORT, !0, c, f);
            f += 4;
            b.vertexAttribPointer(a.vNormal, 2, b.UNSIGNED_SHORT, !0, c, f);
            d && b.vertexAttribPointer(a.vColor, 4, b.UNSIGNED_BYTE, !0, c, f + 4);
            b.drawElements(b.TRIANGLES, this.indexCount, this.mesh.indexType, this.indexOffset);
            b.disableVertexAttribArray(a.vPosition);
            b.disableVertexAttribArray(a.vTexCoord);
            b.disableVertexAttribArray(a.vTangent);
            b.disableVertexAttribArray(a.vBitangent);
            b.disableVertexAttribArray(a.vNormal);
            d && b.disableVertexAttribArray(a.vColor);
            e && b.disableVertexAttribArray(a.vTexCoord2)
        }
    };
    MeshRenderable.prototype.drawShadow = function(a) {
        var b = this.gl;
        this.mesh.desc.cullBackFaces ? (b.enable(b.CULL_FACE), b.cullFace(b.BACK)) : b.disable(b.CULL_FACE);
        b.bindBuffer(b.ELEMENT_ARRAY_BUFFER, this.mesh.indexBuffer);
        b.bindBuffer(b.ARRAY_BUFFER, this.mesh.vertexBuffer);
        b.enableVertexAttribArray(a);
        b.vertexAttribPointer(a, 3, b.FLOAT, !1, this.mesh.stride, 0);
        b.drawElements(b.TRIANGLES, this.indexCount, this.mesh.indexType, this.indexOffset);
        b.disableVertexAttribArray(a)
    };
    MeshRenderable.prototype.drawAlphaShadow = function(a, b) {
        var c = this.gl;
        this.mesh.desc.cullBackFaces ? (c.enable(c.CULL_FACE), c.cullFace(c.BACK)) : c.disable(c.CULL_FACE);
        c.bindBuffer(c.ELEMENT_ARRAY_BUFFER, this.mesh.indexBuffer);
        c.bindBuffer(c.ARRAY_BUFFER, this.mesh.vertexBuffer);
        c.enableVertexAttribArray(a);
        c.enableVertexAttribArray(b);
        c.vertexAttribPointer(a, 3, c.FLOAT, !1, this.mesh.stride, 0);
        c.vertexAttribPointer(b, 2, c.FLOAT, !1, this.mesh.stride, 12);
        c.drawElements(c.TRIANGLES, this.indexCount, this.mesh.indexType,
            this.indexOffset);
        c.disableVertexAttribArray(a);
        c.disableVertexAttribArray(b)
    };
    MeshRenderable.prototype.drawAlphaPrepass = function(a) {
        var b = this.gl;
        if (this.material.bindAlphaPrepass(a)) {
            a = this.material.prepassShader.attribs;
            var c = this.mesh.stride;
            this.mesh.desc.cullBackFaces ? (b.enable(b.CULL_FACE), b.cullFace(b.BACK)) : b.disable(b.CULL_FACE);
            b.bindBuffer(b.ELEMENT_ARRAY_BUFFER, this.mesh.indexBuffer);
            b.bindBuffer(b.ARRAY_BUFFER, this.mesh.vertexBuffer);
            b.enableVertexAttribArray(a.vPosition);
            b.enableVertexAttribArray(a.vTexCoord);
            b.vertexAttribPointer(a.vPosition, 3, b.FLOAT, !1, c, 0);
            b.vertexAttribPointer(a.vTexCoord, 2, b.FLOAT, !1, c, 12);
            b.drawElements(b.TRIANGLES, this.indexCount, this.mesh.indexType, this.indexOffset);
            b.disableVertexAttribArray(a.vPosition);
            b.disableVertexAttribArray(a.vTexCoord)
        }
    };
    MeshRenderable.prototype.drawWire = function() {
        var a = this.material.wireShader.attribs,
            b = this.gl;
        b.enableVertexAttribArray(a.vPosition);
        b.bindBuffer(b.ELEMENT_ARRAY_BUFFER, this.mesh.wireBuffer);
        b.bindBuffer(b.ARRAY_BUFFER, this.mesh.vertexBuffer);
        b.vertexAttribPointer(a.vPosition, 3, b.FLOAT, !1, this.mesh.stride, 0);
        b.drawElements(b.LINES, this.wireIndexCount, this.mesh.indexType, this.wireIndexOffset);
        b.disableVertexAttribArray(a.vPosition)
    };
    MeshRenderable.prototype.complete = function() {
        return this.material.complete()
    };
    var Network = {
        fetchImage: function(a, b, c) {
            var d = new Image;
            d.crossOrigin = "Anonymous";
            d.onload = function() {
                0 < d.width && 0 < d.height ? b(d) : c && c()
            };
            c && (req.onerror = function() {
                c()
            });
            d.src = a
        },
        fetchText: function(a, b, c, d) {
            var e = new XMLHttpRequest;
            e.open("GET", a, !0);
            e.onload = function() {
                200 == e.status ? b(e.responseText) : c && c()
            };
            c && (e.onerror = function() {
                c()
            });
            d && (e.onprogress = function(a) {
                d(a.loaded, a.total)
            });
            e.send()
        },
        fetchBinary: function(a, b, c, d) {
            var e = new XMLHttpRequest;
            e.open("GET", a, !0);
            e.responseType = "arraybuffer";
            e.onload = function() {
                200 == e.status ? b(e.response) : c && c()
            };
            c && (e.onerror = function() {
                c()
            });
            d && (e.onprogress = function(a) {
                d(a.loaded, a.total)
            });
            e.send()
        },
        fetchBinaryIncremental: function(a, b, c, d) {
            var e = new XMLHttpRequest;
            e.open("HEAD", a, !0);
            e.onload = function() {
                if (200 == e.status) {
                    var f = e.getResponseHeader("Accept-Ranges");
                    if (f && "none" != f) {
                        var g = e.getResponseHeader("Content-Length") | 0,
                            h = function(c, e) {
                                var f = new XMLHttpRequest;
                                f.open("GET", a, !0);
                                f.setRequestHeader("Range", "bytes=" + c + "-" + e);
                                f.responseType = "arraybuffer";
                                f.onload = function() {
                                    (206 == f.status || 200 == f.status) && b(f.response) && e < g && (c += d, e += d, e = e < g - 1 ? e : g - 1, h(c, e))
                                };
                                f.send()
                            };
                        h(0, d - 1)
                    } else c && c()
                } else c && c()
            };
            c && (req.onerror = function() {
                c()
            });
            e.send()
        }
    };

    function PostRender(a, b, c) {
        this.gl = a;
        this.desc = b;
        b = [];
        0 != this.desc.sharpen && b.push("#define SHARPEN");
        (this.useBloom = 0 < this.desc.bloomColor[0] * this.desc.bloomColor[3] || 0 < this.desc.bloomColor[1] * this.desc.bloomColor[3] || 0 < this.desc.bloomColor[2] * this.desc.bloomColor[3]) && b.push("#define BLOOM");
        0 != this.desc.vignette[3] && b.push("#define VIGNETTE");
        1 == this.desc.saturation[0] * this.desc.saturation[3] && 1 == this.desc.saturation[1] * this.desc.saturation[3] && 1 == this.desc.saturation[2] * this.desc.saturation[3] ||
            b.push("#define SATURATION");
        1 == this.desc.contrast[0] * this.desc.contrast[3] && 1 == this.desc.contrast[1] * this.desc.contrast[3] && 1 == this.desc.contrast[2] * this.desc.contrast[3] && 1 == this.desc.brightness[0] * this.desc.brightness[3] && 1 == this.desc.brightness[1] * this.desc.brightness[3] && 1 == this.desc.brightness[2] * this.desc.brightness[3] || b.push("#define CONTRAST");
        0 != this.desc.grain && b.push("#define GRAIN");
        1 == this.desc.toneMap ? b.push("#define REINHARD") : 2 == this.desc.toneMap && b.push("#define HEJL");
        this.desc.colorLUT &&
            b.push("#define COLOR_LUT");
        this.sampleCount = 1;
        this.sampleIndex = 0;
        c && (c = [], this.gl.hints.mobile ? (this.sampleCount = 3, this.sampleOffsets = [
            [-0.4375, -0.5625],
            [0.625, -0.25],
            [-0.1875, 0.5]
        ]) : (c.push("#define HIGHQ"), this.sampleCount = 4, this.sampleOffsets = [
            [-0.5, -0.5],
            [0.5, -0.5],
            [-0.5, 0.5],
            [0.5, 0.5]
        ]), this.aaResolve = a.shaderCache.fromURLs("postvert.glsl", "aaresolve.glsl", c));
        this.samplesValid = new Uint8Array(4);
        this.shader = a.shaderCache.fromURLs("postvert.glsl", "postfrag.glsl", b);
        this.plainShader = a.shaderCache.fromURLs("postvert.glsl",
            "postfrag.glsl", []);
        this.fullscreenTriangle = a.createBuffer();
        a.bindBuffer(a.ARRAY_BUFFER, this.fullscreenTriangle);
        c = new Float32Array([0, 0, 2, 0, 0, 2]);
        a.bufferData(a.ARRAY_BUFFER, c, a.STATIC_DRAW);
        a.bindBuffer(a.ARRAY_BUFFER, null);
        if (this.useBloom) {
            this.bloomTextures = [];
            this.bloomTargets = [];
            for (c = 0; 2 > c; ++c) b = {
                    width: 256,
                    height: 256,
                    clamp: !0
                }, this.bloomTextures[c] = new Texture(a, b), this.bloomTextures[c].loadArray(null, a.RGBA, a.ext.textureHalf && a.ext.textureHalfLinear ? a.ext.textureHalf.HALF_FLOAT_OES : a.UNSIGNED_BYTE),
                this.bloomTargets[c] = new Framebuffer(a, {
                    width: b.width,
                    height: b.height,
                    color0: this.bloomTextures[c]
                });
            for (this.bloomSamples = 64; this.bloomSamples + 16 >= a.limits.fragmentUniforms;) this.bloomSamples /= 2;
            this.bloomShader = a.shaderCache.fromURLs("postvert.glsl", "bloom.glsl", ["#define BLOOM_SAMPLES " + this.bloomSamples]);
            this.shrinkShader = a.shaderCache.fromURLs("postvert.glsl", "bloomshrink.glsl")
        }
        a = new Uint8Array(16384);
        for (c = 0; 16384 > c; c++) {
            b = 255 * Math.random();
            var d = 255 * Math.random();
            a[c] = 0.5 * (b + d)
        }
        this.noiseTexture =
            new Texture(this.gl, {
                width: 128,
                height: 128
            });
        this.noiseTexture.loadArray(a, this.gl.LUMINANCE);
        this.desc.colorLUT && (a = this.desc.colorLUT, this.colorLUT = new Texture(this.gl, {
            width: a.length / 3 | 0,
            height: 1,
            clamp: !0
        }), this.colorLUT.loadArray(new Uint8Array(a), this.gl.RGB));
        this.blackTexture = new Texture(this.gl, {
            width: 1,
            height: 1
        });
        this.blackTexture.loadArray(new Uint8Array([0, 0, 0, 0]));
        this.bloomResult = this.blackTexture
    }
    PostRender.prototype.prepareBloom = function(a) {
        if (this.useBloom && this.bloomShader.complete() && this.shrinkShader.complete()) {
            this.shrinkShader.bind();
            this.bloomTargets[1].bind();
            a.bind(this.shrinkShader.samplers.tInput);
            this.fillScreen(this.shrinkShader.attribs.vCoord);
            this.bloomShader.bind();
            var b = [];
            this.bloomTargets[0].bind();
            this.bloomTextures[1].bind(this.bloomShader.samplers.tInput);
            for (var c = 0, d = 0; d < this.bloomSamples; ++d) {
                var e = -1 + 2 * d / (this.bloomSamples - 1),
                    f;
                f = 4 * e;
                f = Math.exp(-0.5 * f * f / 1) / 2.50662827463;
                c += f;
                b[4 * d + 0] = e * this.desc.bloomSize;
                b[4 * d + 1] = 0;
                b[4 * d + 2] = f;
                b[4 * d + 3] = 0
            }
            for (d = 0; d < this.bloomSamples; ++d) b[4 * d + 2] /= c;
            this.gl.uniform4fv(this.bloomShader.params.uKernel, b);
            this.fillScreen(this.bloomShader.attribs.vCoord);
            this.bloomTargets[1].bind();
            this.bloomTextures[0].bind(this.bloomShader.samplers.tInput);
            for (d = 0; d < this.bloomSamples; ++d) c = b[4 * d + 0], c *= a.desc.width / a.desc.height, b[4 * d + 0] = 0, b[4 * d + 1] = c;
            this.gl.uniform4fv(this.bloomShader.params.uKernel, b);
            this.fillScreen(this.bloomShader.attribs.vCoord);
            this.bloomResult = this.bloomTextures[1]
        } else this.bloomResult = this.blackTexture
    };
    PostRender.prototype.computeParams = function(a, b) {
        var c = this.desc,
            d = {};
        d.scale = [c.contrast[0] * c.contrast[3], c.contrast[1] * c.contrast[3], c.contrast[2] * c.contrast[3]];
        d.bias = [c.bias[0] * c.bias[3], c.bias[1] * c.bias[3], c.bias[2] * c.bias[3]];
        d.bias = [-d.bias[0] * d.scale[0] + d.bias[0], -d.bias[1] * d.scale[1] + d.bias[1], -d.bias[2] * d.scale[2] + d.bias[2]];
        var e = [c.brightness[0] * c.brightness[3], c.brightness[1] * c.brightness[3], c.brightness[2] * c.brightness[3]];
        d.scale = [d.scale[0] * e[0], d.scale[1] * e[1], d.scale[2] * e[2]];
        d.bias = [d.bias[0] * e[0], d.bias[1] * e[1], d.bias[2] * e[2]];
        d.saturation = [c.saturation[0] * c.saturation[3], c.saturation[1] * c.saturation[3], c.saturation[2] * c.saturation[3]];
        d.bloomColor = [c.bloomColor[0] * c.bloomColor[3], c.bloomColor[1] * c.bloomColor[3], c.bloomColor[2] * c.bloomColor[3]];
        d.sharpen = [c.sharpen, 0.25 * c.sharpen, c.sharpenLimit];
        d.sharpenKernel = [1 / a, 0, 0, 1 / b];
        e = a > b ? a : b;
        d.vignetteAspect = [a / e, b / e, 0.5 * a / e, 0.5 * b / e];
        d.vignette = [2 * (1 - c.vignette[0]) * c.vignette[3], 2 * (1 - c.vignette[1]) * c.vignette[3], 2 * (1 - c.vignette[2]) *
            c.vignette[3], c.vignetteCurve
        ];
        var e = 1 / this.noiseTexture.desc.width,
            f = 1 / this.noiseTexture.desc.height,
            g = 1 - c.grainSharpness;
        d.grainCoord = [e * a, f * b, 0.5 * g * e, 0.5 * g * f];
        d.grainScaleBias = [2 * c.grain, -c.grain];
        return d
    };
    PostRender.prototype.present = function(a, b, c, d) {
        1 < this.sampleCount && this.allocAABuffers(a.desc.width, a.desc.height);
        d || this.prepareBloom(a);
        var e = d ? this.plainShader : this.shader;
        if (e.bind()) {
            d = this.gl;
            var f = e.samplers,
                g = e.params,
                h = this.computeParams(b, c);
            a.bind(f.tInput);
            this.bloomResult.bind(f.tBloom);
            this.noiseTexture.bind(f.tGrain);
            this.colorLUT && this.colorLUT.bind(f.tLUT);
            d.uniform3fv(g.uScale, h.scale);
            d.uniform3fv(g.uBias, h.bias);
            d.uniform3fv(g.uSaturation, h.saturation);
            d.uniform4fv(g.uSharpenKernel,
                h.sharpenKernel);
            d.uniform3fv(g.uSharpness, h.sharpen);
            d.uniform3fv(g.uBloomColor, h.bloomColor);
            d.uniform4fv(g.uVignetteAspect, h.vignetteAspect);
            d.uniform4fv(g.uVignette, h.vignette);
            d.uniform4fv(g.uGrainCoord, h.grainCoord);
            d.uniform2fv(g.uGrainScaleBias, h.grainScaleBias);
            if (this.aaResolve) {
                this.sampleFramebuffers[this.sampleIndex].bind();
                this.fillScreen(e.attribs.vCoord);
                this.samplesValid[this.sampleIndex] = 1;
                Framebuffer.bindNone(d);
                d.viewport(0, 0, b, c);
                this.aaResolve.bind();
                for (b = a = 0; b < this.sampleCount; ++b) a +=
                    this.samplesValid[b], this.sampleTextures[b].bind(this.aaResolve.samplers["tInput" + b]);
                a = 1 / a;
                d.uniform4fv(this.aaResolve.params.uSamplesValid, [this.samplesValid[0] ? a : 0, this.samplesValid[1] ? a : 0, this.samplesValid[2] ? a : 0, this.samplesValid[3] ? a : 0]);
                this.fillScreen(this.aaResolve.attribs.vCoord);
                this.sampleIndex = (this.sampleIndex + 1) % this.sampleCount
            } else Framebuffer.bindNone(d), d.viewport(0, 0, b, c), this.fillScreen(e.attribs.vCoord)
        }
    };
    PostRender.prototype.allocAABuffers = function(a, b) {
        if (void 0 === this.sampleTextures || this.sampleTextures[0].desc.width != a || this.sampleTextures[0].desc.height != b) {
            this.sampleTextures = [];
            this.sampleFramebuffers = [];
            for (var c = 0; c < this.sampleCount; ++c) {
                var d = new Texture(this.gl, {
                    width: a,
                    height: b,
                    nofilter: !0
                });
                d.loadArray();
                this.sampleTextures.push(d);
                this.sampleFramebuffers.push(new Framebuffer(this.gl, {
                    width: a,
                    height: b,
                    color0: d,
                    ignoreStatus: !0
                }))
            }
            this.discardAAHistory()
        }
    };
    PostRender.prototype.adjustProjectionForSupersampling = function(a) {
        if (1 < this.sampleCount) {
            var b = this.sampleOffsets[this.sampleIndex][0] / a.size[0],
                c = this.sampleOffsets[this.sampleIndex][1] / a.size[1],
                b = Matrix.translation(Matrix.empty(), b, c, 0);
            Matrix.mul(a.projectionMatrix, b, a.projectionMatrix)
        }
    };
    PostRender.prototype.discardAAHistory = function() {
        for (var a = this.sampleIndex = 0; a < this.samplesValid.length; ++a) this.samplesValid[a] = 0
    };
    PostRender.prototype.fillScreen = function(a) {
        var b = this.gl;
        b.bindBuffer(b.ARRAY_BUFFER, this.fullscreenTriangle);
        b.enableVertexAttribArray(a);
        b.vertexAttribPointer(a, 2, b.FLOAT, !1, 0, 0);
        b.drawArrays(b.TRIANGLES, 0, 3);
        b.disableVertexAttribArray(a);
        b.bindBuffer(b.ARRAY_BUFFER, null)
    };

    function Scene(a) {
        this.gl = a;
        this.name = "untitled";
        this.meshes = [];
        this.meshRenderables = [];
        this.materials = {};
        this.nextView = this.sky = this.view = null;
        this.viewFade = 0;
        this.shadow = this.stripData = this.lights = null
    }
    Scene.prototype.load = function(a) {
        var b = this.gl,
            c;
        c = a.extract("scene.json");
        if (void 0 !== c) {
            if (!a.checkSignature(c)) return !1;
            c = (new ByteStream(c.data)).asString();
            if (null == c || 0 >= c.length) return !1;
            c = JSON.parse(c)
        } else return !1;
        this.metaData = c.metaData;
        this.view = new View(c.mainCamera.view);
        this.sky = new Sky(this.gl, a, c.sky);
        this.lights = new Lights(c.lights, this.view);
        this.materials = {};
        for (var d in c.materials) {
            var e = c.materials[d];
            e.lightCount = this.lights.count;
            e.shadowCount = this.lights.shadowCount;
            this.materials[e.name] =
                new Material(this.gl, a, e)
        }
        if (c.meshes)
            for (e = 0; e < c.meshes.length; ++e) {
                d = c.meshes[e];
                d = new Mesh(this.gl, d, a.extract(d.file));
                this.meshes.push(d);
                for (var f = 0; f < d.desc.subMeshes.length; ++f) {
                    var g = d.desc.subMeshes[f];
                    this.meshRenderables.push(new MeshRenderable(d, g, this.materials[g.material]))
                }
            }
        this.bounds = new Bounds(this.meshes);
        this.postRender = new PostRender(this.gl, c.mainCamera.post, !0);
        this.shadow = new ShadowCollector(b, this.lights.shadowCount);
        this.cameras = c.Cameras;
        return !0
    };
    Scene.prototype.update = function() {
        this.lights.update(this.view, this.bounds)
    };
    Scene.prototype.collectShadows = function(a) {
        this.shadow.collect(this, a)
    };
    Scene.prototype.draw = function() {
        var a = this.gl;
        this.sky.setClearColor();
        a.clear(a.COLOR_BUFFER_BIT | a.DEPTH_BUFFER_BIT | a.STENCIL_BUFFER_BIT);
        a.enable(a.DEPTH_TEST);
        this.sky.draw(this);
        for (var b = 0; b < this.meshRenderables.length; ++b) this.meshRenderables[b].material.usesBlending || this.meshRenderables[b].draw(this);
        a.enable(a.POLYGON_OFFSET_FILL);
        a.polygonOffset(1, 1);
        a.colorMask(!1, !1, !1, !1);
        for (b = 0; b < this.meshRenderables.length; ++b) this.meshRenderables[b].drawAlphaPrepass(this);
        a.colorMask(!0, !0, !0, !0);
        a.disable(a.POLYGON_OFFSET_FILL);
        a.depthFunc(a.LEQUAL);
        a.depthMask(!1);
        for (b = 0; b < this.meshRenderables.length; ++b) this.meshRenderables[b].material.usesBlending && this.meshRenderables[b].draw(this);
        a.depthMask(!0);
        a.depthFunc(a.LESS);
        if (this.stripData.activeWireframe() && 0 < this.meshRenderables.length) {
            this.meshRenderables[0].material.bindWire(this);
            for (b = 0; b < this.meshRenderables.length; ++b) this.meshRenderables[b].drawWire();
            a.depthMask(!0)
        }
        a.disable(a.BLEND)
    };
    Scene.prototype.complete = function() {
        if (!this.sky.complete() || !this.shadow.complete()) return !1;
        for (var a = 0; a < this.meshRenderables.length; ++a)
            if (!this.meshRenderables[a].complete()) return !1;
        return !0
    };

    function Shader(a) {
        this.gl = a;
        this.program = null;
        this.params = {};
        this.samplers = {};
        this.attribs = {}
    }
    Shader.prototype.build = function(a, b) {
        var c = this.gl;
        this.program = c.createProgram();
        this.params = {};
        this.samplers = {};
        this.attribs = {};
        var d = function(a) {
                for (var b = "", c = a.indexOf("\n"), d = 0; - 1 != c;) d++, b += d + ": ", b += a.substring(0, c + 1), a = a.substring(c + 1, a.length), c = a.indexOf("\n");
                console.log(b)
            },
            e = c.createShader(c.VERTEX_SHADER);
        c.shaderSource(e, a);
        c.compileShader(e);
        c.getShaderParameter(e, c.COMPILE_STATUS) || (console.log(c.getShaderInfoLog(e)), marmoset.verboseErrors && d(a));
        c.attachShader(this.program, e);
        e =
            c.createShader(c.FRAGMENT_SHADER);
        c.shaderSource(e, b);
        c.compileShader(e);
        c.getShaderParameter(e, c.COMPILE_STATUS) || (console.log(c.getShaderInfoLog(e)), marmoset.verboseErrors && d(b));
        c.attachShader(this.program, e);
        c.linkProgram(this.program);
        c.getProgramParameter(this.program, c.LINK_STATUS) || console.log(c.getProgramInfoLog(this.program));
        for (var e = c.getProgramParameter(this.program, c.ACTIVE_UNIFORMS), f = 0, d = 0; d < e; ++d) {
            var g = c.getActiveUniform(this.program, d),
                h = g.name,
                k = h.indexOf("[");
            0 <= k && (h = h.substring(0,
                k));
            k = c.getUniformLocation(this.program, g.name);
            g.type == c.SAMPLER_2D || g.type == c.SAMPLER_CUBE ? this.samplers[h] = {
                location: k,
                unit: f++
            } : this.params[h] = k
        }
        e = c.getProgramParameter(this.program, c.ACTIVE_ATTRIBUTES);
        for (d = 0; d < e; ++d) f = c.getActiveAttrib(this.program, d), this.attribs[f.name] = c.getAttribLocation(this.program, f.name)
    };
    Shader.prototype.bind = function() {
        return this.program ? (this.gl.useProgram(this.program), !0) : !1
    };
    Shader.prototype.complete = function() {
        return !!this.program
    };

    function ShaderCache(a) {
        this.gl = a;
        this.cache = []
    }
    ShaderCache.prototype.fromURLs = function(a, b, c) {
        var d = "";
        if (c)
            for (var e = 0; e < c.length; ++e) d = c[e] + "\n" + d;
        c = d + ":" + a + "|" + b;
        e = this.cache[c];
        if (void 0 !== e) return e;
        var f = new Shader(this.gl),
            g = null,
            h = null,
            k = function() {
                null != g && null != h && f.build(g, h)
            };
        this.fetch(a, function(a) {
            g = d + a;
            k()
        });
        this.fetch(b, function(a) {
            h = d + a;
            k()
        });
        return this.cache[c] = f
    };
    ShaderCache.prototype.fetch = function(a, b) {
        "undefined" != typeof ShaderTable ? void 0 !== ShaderTable[a] ? this.resolveIncludes(new String(ShaderTable[a]), b) : b("") : Network.fetchText("src/shader/" + a, function(a) {
            this.resolveIncludes(a, b)
        }.bind(this), function() {
            b("")
        })
    };
    ShaderCache.prototype.resolveIncludes = function(a, b) {
        for (var c = [], d = !0, e = function(a, b, e, f, m) {
                d = !0;
                c.push({
                    offset: m,
                    path: b.slice(1, b.length - 1)
                });
                return ""
            }; d;) d = !1, a = a.replace(/#include\s((<[^>]+>)|("[^"]+"))/, e);
        if (0 < c.length)
            for (var f = c.length, e = 0; e < c.length; ++e) this.fetch(c[e].path, function(d) {
                this.src = d;
                if (0 >= --f) {
                    for (d = c.length - 1; 0 <= d; --d) a = a.substring(0, c[d].offset) + c[d].src + a.substring(c[d].offset);
                    b(a)
                }
            }.bind(c[e]));
        else b(a)
    };

    function ShadowCollector(a, b) {
        this.gl = a;
        this.shadowCount = b;
        this.desc = c;
        this.shaderSolid = a.shaderCache.fromURLs("shadowvert.glsl", "shadowfrag.glsl");
        this.shaderAlphaTest = a.shaderCache.fromURLs("shadowvert.glsl", "shadowfrag.glsl", ["#define ALPHA_TEST 1"]);
        this.depthTextures = [];
        this.depthTargets = [];
        if (0 < this.shadowCount) {
            var c = {
                width: 2048,
                height: 2048,
                clamp: !0,
                mipmap: !1,
                nofilter: !0
            };
            a.hints.mobile && (c.width = c.height = 1536);
            for (var d = {
                    width: c.width,
                    height: c.height,
                    depthBuffer: Framebuffer.createDepthBuffer(a,
                        c.width, c.height)
                }, e = a.RGB, f = a.UNSIGNED_BYTE, g = 0; g < this.shadowCount; ++g) this.depthTextures[g] = new Texture(a, c), this.depthTextures[g].loadArray(null, e, f), d.color0 = this.depthTextures[g], this.depthTargets[g] = new Framebuffer(a, d)
        }
    }
    ShadowCollector.prototype.bindDepthTexture = function(a, b) {
        this.shadowCount > b && this.depthTextures[b].bind(a)
    };
    ShadowCollector.prototype.collect = function(a, b) {
        var c = this.gl,
            d = a.lights,
            e = d.shadowCount,
            f = d.modelViewBuffer,
            g = d.projectionBuffer,
            h = d.matrix;
        if (!(0 >= e)) {
            for (var k = Matrix.empty(), l = !1, m = 0; m < e; ++m)
                if (d.shadowsNeedUpdate[m]) {
                    d.shadowsNeedUpdate[m] = 0;
                    l = !0;
                    Matrix.mul(k, f.subarray(16 * m, 16 * (m + 1)), h);
                    Matrix.mul(k, g.subarray(16 * m, 16 * (m + 1)), k);
                    this.depthTargets[m].bind();
                    c.clearColor(1, 1, 1, 1);
                    c.clear(c.COLOR_BUFFER_BIT | c.DEPTH_BUFFER_BIT);
                    var n = this.shaderSolid;
                    n.bind();
                    c.uniformMatrix4fv(n.params.uViewProjection, !1, k);
                    for (var r = 0; r < a.meshRenderables.length; ++r) {
                        var p = a.meshRenderables[r],
                            q = p.material;
                        p.mesh.desc.castShadows && q.castShadows && (0 < q.shadowAlphaTest || p.drawShadow(n.attribs.vPosition))
                    }
                    n = this.shaderAlphaTest;
                    n.bind();
                    c.uniformMatrix4fv(n.params.uViewProjection, !1, k);
                    for (r = 0; r < a.meshRenderables.length; ++r) p = a.meshRenderables[r], q = p.material, p.mesh.desc.castShadows && q.castShadows && 0 < q.shadowAlphaTest && (q.textures.albedo.bind(n.samplers.tAlbedo), p.drawAlphaShadow(n.attribs.vPosition, n.attribs.vTexCoord))
                }
            l &&
                (b.bind(), c.enable(c.CULL_FACE), c.cullFace(c.BACK))
        }
    };
    ShadowCollector.prototype.complete = function() {
        return this.shaderSolid.complete() && this.shaderAlphaTest.complete()
    };

    function Sky(a, b, c) {
        this.gl = a;
        var d = b.extract("sky.dat") || b.extract("sky.png");
        if (void 0 !== d) {
            this.specularTexture = new Texture(a, {
                width: 256,
                height: 2048,
                clamp: !0
            });
            b = d.data;
            for (var d = d.data.length, e = d / 4, f = new Uint8Array(d), g = 0, h = 0; g < d; ++h) f[g++] = b[h + 2 * e], f[g++] = b[h + e], f[g++] = b[h], f[g++] = b[h + 3 * e];
            this.specularTexture.loadArray(f)
        }
        this.diffuseCoefficients = new Float32Array(c.diffuseCoefficients);
        this.backgroundMode = c.backgroundMode || 0;
        this.backgroundBrightness = c.backgroundBrightness || 1;
        this.backgroundColor =
            new Float32Array(c.backgroundColor);
        if (1 <= this.backgroundMode)
            if (this.backgroundShader = a.shaderCache.fromURLs("skyvert.glsl", 3 == this.backgroundMode ? "skySH.glsl" : "sky.glsl", ["#define SKYMODE " + this.backgroundMode]), this.vertexBuffer = a.createBuffer(), a.bindBuffer(a.ARRAY_BUFFER, this.vertexBuffer), c = 1 / 256, b = 0.5 / 256, d = 2.8 * b, e = 0.5 * b, c = new Float32Array([0, 1, 0, 0.49609375 + c, 0.49609375 + c, 1, 0, 0, 0.9921875 + c, 0.49609375 + c, 0, 0, 1, 0.49609375 + c, 0.9921875 + c, -1, 0, 0, 0 + c, 0.49609375 + c, 0, 0, -1, 0.49609375 + c, 0 + c, 0, -1, 0, 0.9921875 +
                    c, 0 + c, 0, -1, 0, 0.9921875 + c, 0.9921875 + c, 0, -1, 0, 0 + c, 0.9921875 + c, 0, -1, 0, 0 + c, 0 + c, d, 1 - d, -d, 0.5 + b, 0.5 - b, d, 1 - d, d, 0.5 + b, 0.5 + b, -d, 1 - d, d, 0.5 - b, 0.5 + b, -d, 1 - d, -d, 0.5 - b, 0.5 - b, -d, 0, -1 + d, 0.5 - b, 0 + c + b, d, 0, -1 + d, 0.5 + b, 0 + c + b, 1 - d, 0, -d, 0.9921875 + c - b, 0.5 - b, 1 - d, 0, d, 0.9921875 + c - b, 0.5 + b, d, 0, 1 - d, 0.5 + b, 0.9921875 + c - b, -d, 0, 1 - d, 0.5 - b, 0.9921875 + c - b, -1 + d, 0, d, 0 + c + b, 0.5 + b, -1 + d, 0, -d, 0 + c + b, 0.5 - b, 1, 0, 0, 0.9921875 + c - e, 0.49609375 + c, 0, 0, 1, 0.49609375 + c, 0.9921875 + c - e, -1, 0, 0, 0 + c + e, 0.49609375 + c, 0, 0, -1, 0.49609375 + c, 0 + c + e, 0, 1, 0, 0.49609375 + c - e, 0.49609375 +
                    c, 0, 1, 0, 0.49609375 + c, 0.49609375 + c - e, 0, 1, 0, 0.49609375 + c + e, 0.49609375 + c, 0, 1, 0, 0.49609375 + c, 0.49609375 + c + e
                ]), a.bufferData(a.ARRAY_BUFFER, c, a.STATIC_DRAW), a.bindBuffer(a.ARRAY_BUFFER, null), this.indexBuffer = a.createBuffer(), a.bindBuffer(a.ELEMENT_ARRAY_BUFFER, this.indexBuffer), c = new Uint16Array([2, 1, 6, 3, 2, 7, 8, 4, 3, 4, 5, 1, 9, 14, 15, 17, 10, 16, 18, 19, 11, 20, 13, 12, 28, 12, 13, 13, 24, 28, 28, 24, 9, 9, 24, 14, 25, 9, 15, 25, 15, 21, 10, 25, 21, 10, 21, 16, 22, 26, 10, 22, 10, 17, 18, 11, 26, 22, 18, 26, 19, 23, 27, 19, 27, 11, 23, 20, 27, 27, 20, 12]), this.skyIndexCount =
                c.length, a.bufferData(a.ELEMENT_ARRAY_BUFFER, c, a.STATIC_DRAW), a.bindBuffer(a.ELEMENT_ARRAY_BUFFER, null), 3 == this.backgroundMode)
                for (this.backgroundCoefficients = new Float32Array(this.diffuseCoefficients), g = 0; g < this.backgroundCoefficients.length; ++g) this.backgroundCoefficients[g] *= this.backgroundBrightness;
            else {
                this.backgroundTexture = new Texture(a, {
                    width: 256,
                    height: 256,
                    clamp: !0
                });
                c = !1;
                var k;
                a.ext.textureHalf && a.ext.textureHalfLinear && (this.backgroundTexture.loadArray(null, a.RGB, a.ext.textureHalf.HALF_FLOAT_OES),
                    k = new Framebuffer(a, {
                        color0: this.backgroundTexture
                    }), c = k.valid);
                !c && a.ext.textureFloat && a.ext.textureFloatLinear && !a.hints.mobile && (this.backgroundTexture.loadArray(null, a.RGB, a.FLOAT), k = new Framebuffer(a, {
                    color0: this.backgroundTexture
                }), c = k.valid);
                c || (this.backgroundTexture.loadArray(), k = new Framebuffer(a, {
                    color0: this.backgroundTexture
                }));
                k.bind();
                k = new Shader(a);
                k.build("precision highp float; varying vec2 tc; attribute vec4 p; void main(){ gl_Position=p; tc=vec2(0.5,0.5/8.0)*p.xy+vec2(0.5,6.5/8.0); }",
                    "precision highp float; varying vec2 tc; uniform sampler2D tex; uniform float b; void main(){vec4 s=texture2D(tex,tc); gl_FragColor.xyz=s.xyz*(b*s.w);}");
                k.bind();
                a.uniform1f(k.params.b, 7 * Math.sqrt(this.backgroundBrightness));
                this.specularTexture.bind(k.samplers.tex);
                c = a.createBuffer();
                a.bindBuffer(a.ARRAY_BUFFER, c);
                c = new Float32Array([-1, -1, 0.5, 1, 3, -1, 0.5, 1, -1, 3, 0.5, 1]);
                a.bufferData(a.ARRAY_BUFFER, c, a.STATIC_DRAW);
                a.enableVertexAttribArray(k.attribs.p);
                a.vertexAttribPointer(k.attribs.p, 4, a.FLOAT, !1, 0, 0);
                a.drawArrays(a.TRIANGLES, 0, 3);
                a.disableVertexAttribArray(k.attribs.p)
            }
    }
    Sky.prototype.setClearColor = function() {
        if (1 > this.backgroundMode) {
            var a = this.backgroundColor;
            this.gl.clearColor(a[0], a[1], a[2], 1)
        } else this.gl.clearColor(0.0582, 0.06772, 0.07805, 1)
    };
    Sky.prototype.draw = function(a) {
        if (1 > this.backgroundMode) return !1;
        if (this.complete()) {
            var b = this.gl,
                c = this.backgroundShader,
                d = a.view,
                e = a.lights.invMatrix;
            c.bind();
            b.uniformMatrix4fv(c.params.uInverseSkyMatrix, !1, e);
            b.uniformMatrix4fv(c.params.uViewProjection, !1, d.viewProjectionMatrix);
            3 == this.backgroundMode ? b.uniform4fv(c.params.uSkyCoefficients, this.backgroundCoefficients) : this.backgroundTexture.bind(c.samplers.tSkyTexture);
            a = 0.07 + 0.94 * (1 - a.stripData.activeFade());
            b.uniform1f(c.params.uAlpha, a);
            b.bindBuffer(b.ARRAY_BUFFER,
                this.vertexBuffer);
            b.enableVertexAttribArray(c.attribs.vPosition);
            b.vertexAttribPointer(c.attribs.vPosition, 3, b.FLOAT, !1, 20, 0);
            b.enableVertexAttribArray(c.attribs.vTexCoord);
            b.vertexAttribPointer(c.attribs.vTexCoord, 2, b.FLOAT, !1, 20, 12);
            b.bindBuffer(b.ELEMENT_ARRAY_BUFFER, this.indexBuffer);
            1 > a && (b.enable(b.BLEND), b.blendFunc(b.SRC_ALPHA, b.ONE_MINUS_SRC_ALPHA));
            b.depthMask(!1);
            b.disable(b.DEPTH_TEST);
            b.drawElements(b.TRIANGLES, this.skyIndexCount, b.UNSIGNED_SHORT, 0);
            b.enable(b.DEPTH_TEST);
            b.depthMask(!0);
            1 > a && b.disable(b.BLEND);
            b.disableVertexAttribArray(c.attribs.vPosition);
            b.disableVertexAttribArray(c.attribs.vTexCoord)
        }
    };
    Sky.prototype.complete = function() {
        return this.backgroundShader && !this.backgroundShader.complete() ? !1 : this.specularTexture.complete()
    };

    function StripData() {
        this.STRIP_NONE = -2;
        this.STRIP_MENU = -1;
        this.stripCount = 5;
        this.strips = [0, 0, 0, 0, 0];
        this.labels = ["Normals", "Albedo", "Reflectivity", "Gloss", "Topology"];
        this.stripSlant = 0.25;
        this.selectedStrip = this.STRIP_NONE;
        this.animationActive = !1;
        this.timestamp = Date.now();
        this.update(!0)
    }
    StripData.expDecay = function(a, b) {
        return Math.exp(-0.69314718 / a * b)
    };
    StripData.prototype.update = function(a) {
        var b = 0.001 * (Date.now() - this.timestamp);
        this.timestamp = Date.now();
        for (var c = !1, d = 0; d < this.stripCount; ++d) {
            var e = 0,
                e = this.selectedStrip == this.STRIP_MENU ? -0.9 + 0.3 * (d + 1) : 0 > this.selectedStrip || d < this.selectedStrip ? -2 : 2;
            if (a) this.strips[d] = e;
            else {
                var f = e - this.strips[d],
                    f = f * StripData.expDecay(0.05, b);
                this.animationActive && (this.strips[d] = e - f);
                c = c || 1E-4 < Math.abs(f)
            }
        }
        this.animationActive = c
    };
    StripData.prototype.active = function() {
        return this.selectedStrip >= this.STRIP_MENU
    };
    StripData.prototype.activeFade = function() {
        var a = (this.strips[this.stripCount - 1] - -2) / (-0.9 + 0.3 * this.stripCount - -2),
            a = 1 < a ? 1 : a;
        return 0 > a ? 0 : a
    };
    StripData.prototype.activeWireframe = function() {
        return this.active() && 0.01 < Math.abs(this.strips[4] - this.strips[3])
    };
    StripData.prototype.toggleMenu = function() {
        this.selectedStrip = this.selectedStrip == this.STRIP_MENU ? this.STRIP_NONE : this.STRIP_MENU
    };
    StripData.prototype.selectStrip = function(a, b) {
        if (this.selectedStrip == this.STRIP_MENU) {
            var c = a + b * this.stripSlant;
            this.selectedStrip = this.STRIP_NONE;
            for (var d = 0; d < this.stripCount; ++d)
                if (c < this.strips[d]) {
                    this.selectedStrip = d;
                    break
                }
        } else this.selectedStrip = this.STRIP_MENU
    };

    function Texture(a, b) {
        this.gl = a;
        this.type = a.TEXTURE_2D;
        this.id = null;
        b = b || {};
        this.desc = {
            width: b.width || 1,
            height: b.height || 1,
            mipmap: b.mipmap,
            clamp: b.clamp,
            mirror: b.mirror,
            aniso: b.aniso,
            nofilter: b.nofilter
        }
    }
    Texture.prototype.loadImage = function(a, b) {
        var c = this.gl;
        a && a.width && a.height && (this.desc.width = a.width, this.desc.height = a.height);
        this.id = c.createTexture();
        c.bindTexture(this.type, this.id);
        c.pixelStorei(c.UNPACK_FLIP_Y_WEBGL, !0);
        c.texImage2D(this.type, 0, b || c.RGBA, b || c.RGBA, c.UNSIGNED_BYTE, a);
        this.setParams();
        c.bindTexture(this.type, null)
    };
    Texture.prototype.loadArray = function(a, b, c) {
        var d = this.gl;
        this.id = d.createTexture();
        d.bindTexture(this.type, this.id);
        d.pixelStorei(d.UNPACK_FLIP_Y_WEBGL, !0);
        d.texImage2D(this.type, 0, b || d.RGBA, this.desc.width, this.desc.height, 0, b || d.RGBA, c || d.UNSIGNED_BYTE, a || null);
        this.setParams();
        d.bindTexture(this.type, null)
    };
    Texture.prototype.setParams = function() {
        var a = this.gl,
            b = function(a) {
                return 0 < a && 0 == (a & a - 1)
            };
        b(this.desc.width) && b(this.desc.height) || (this.desc.clamp = !0, this.desc.mipmap = !1);
        b = !this.desc.nofilter;
        this.desc.mipmap ? (a.generateMipmap(this.type), a.texParameteri(this.type, a.TEXTURE_MIN_FILTER, b ? a.LINEAR_MIPMAP_LINEAR : a.NEAREST_MIPMAP_NEAREST)) : a.texParameteri(this.type, a.TEXTURE_MIN_FILTER, b ? a.LINEAR : a.NEAREST);
        a.texParameteri(this.type, a.TEXTURE_MAG_FILTER, b ? a.LINEAR : a.NEAREST);
        if (this.desc.clamp || this.desc.mirror) b =
            this.desc.clamp ? a.CLAMP_TO_EDGE : a.MIRRORED_REPEAT, a.texParameteri(this.type, a.TEXTURE_WRAP_S, b), a.texParameteri(this.type, a.TEXTURE_WRAP_T, b);
        this.desc.aniso && a.ext.textureAniso && a.texParameteri(this.type, a.ext.textureAniso.TEXTURE_MAX_ANISOTROPY_EXT, this.desc.aniso)
    };
    Texture.prototype.rebuildMips = function() {
        this.desc.mipmap && (this.gl.bindTexture(this.type, this.id), this.gl.generateMipmap(this.type))
    };
    Texture.prototype.bind = function(a) {
        if (a) {
            var b = this.gl;
            b.uniform1i(a.location, a.unit);
            b.activeTexture(b.TEXTURE0 + a.unit);
            b.bindTexture(this.type, this.id)
        }
    };
    Texture.prototype.destroy = function() {
        this.gl.deleteTexture(this.id);
        this.id = null
    };
    Texture.prototype.complete = function() {
        return !!this.id
    };

    function TextureCache(a) {
        this.gl = a;
        this.cache = []
    }
    TextureCache.prototype.fromURL = function(a, b) {
        var c = this.cache[a];
        if (void 0 !== c) return c;
        var d = new Texture(this.gl, b);
        Network.fetchImage(a, function(a) {
            d.loadImage(a)
        });
        return this.cache[a] = d
    };
    TextureCache.prototype.fromFile = function(a, b) {
        if (!a) return null;
        var c = this.cache[a.name];
        if (void 0 !== c) return c;
        var d = new Texture(this.gl, b);
        this.cache[a.name] = d;
        TextureCache.parseFile(a, function(a) {
            d.loadImage(a)
        });
        return d
    };
    TextureCache.prototype.fromFilesMergeAlpha = function(a, b, c) {
        if (!b) return this.fromFile(a, c);
        var d = a.name + "|" + b.name,
            e = this.cache[d];
        if (void 0 !== e) return e;
        var f = this.gl;
        this.mergeShader || (this.mergeShader = new Shader(this.gl), this.mergeShader.build("precision highp float; varying vec2 c; attribute vec2 pos; void main(){ gl_Position.xy = 2.0*pos-vec2(1.0); gl_Position.zw = vec2(0.5,1.0); c=pos; }", "precision highp float; varying vec2 c; uniform sampler2D tRGB,tA; void main(){ gl_FragColor.xyz=texture2D(tRGB,c).xyz; gl_FragColor.w=texture2D(tA,c).x; }"),
            this.mergeVerts = f.createBuffer(), f.bindBuffer(f.ARRAY_BUFFER, this.mergeVerts), e = new Float32Array([0, 0, 2, 0, 0, 2]), f.bufferData(f.ARRAY_BUFFER, e, f.STATIC_DRAW), f.bindBuffer(f.ARRAY_BUFFER, null));
        var g = new Texture(this.gl, c);
        this.cache[d] = g;
        var h = 0,
            k = 0,
            l = this.mergeShader,
            m = this.mergeVerts,
            n = function() {
                if (h && k) {
                    var a = h.width > k.width ? h.width : k.width,
                        b = h.height > k.height ? h.height : k.height;
                    g.desc.width = a;
                    g.desc.height = b;
                    if (a <= f.limits.viewportSizes[0] && b <= f.limits.viewportSizes[1]) g.loadArray(null), (new Framebuffer(f, {
                        color0: g,
                        ignoreStatus: !0
                    })).bind(), b = {
                        clamp: !0
                    }, a = new Texture(f, b), a.loadImage(h, f.RGB), b = new Texture(f, b), b.loadImage(k, f.RGB), l.bind(), a.bind(l.samplers.tRGB), b.bind(l.samplers.tA), f.bindBuffer(f.ARRAY_BUFFER, m), f.enableVertexAttribArray(l.attribs.pos), f.vertexAttribPointer(l.attribs.pos, 2, f.FLOAT, !1, 0, 0), f.drawArrays(f.TRIANGLES, 0, 3), f.disableVertexAttribArray(l.attribs.pos), f.bindBuffer(f.ARRAY_BUFFER, null), a.destroy(), b.destroy(), Framebuffer.bindNone(f), g.rebuildMips();
                    else {
                        var c = document.createElement("canvas");
                        c.width = a;
                        c.height = b;
                        var d = c.getContext("2d");
                        d.drawImage(h, 0, 0);
                        c = d.getImageData(0, 0, a, b);
                        c = new Uint8Array(c.data.buffer, c.data.byteOffset, c.data.length);
                        d.drawImage(k, 0, 0);
                        d = d.getImageData(0, 0, a, b).data;
                        a = a * b * 4;
                        for (b = 0; b < a; b += 4) c[b + 3] = d[b];
                        g.loadArray(c)
                    }
                }
            };
        TextureCache.parseFile(a, function(a) {
            h = a;
            n()
        });
        TextureCache.parseFile(b, function(a) {
            k = a;
            n()
        });
        return g
    };
    TextureCache.parseFile = function(a, b, c) {
        var d = c || new Image;
        if ("undefined" != typeof URL && "undefined" != typeof URL.createObjectURL) {
            a = new Blob([a.data], {
                type: a.type
            });
            var e = URL.createObjectURL(a);
            d.onload = function() {
                URL.revokeObjectURL(e);
                b && b(d)
            };
            d.src = e
        } else {
            a = new Blob([a.data], {
                type: a.type
            });
            var f = new FileReader;
            f.onload = function(a) {
                d.src = f.result
            };
            d.onload = function() {
                b && b(d)
            };
            f.readAsDataURL(a)
        }
    };

    function UI(a) {
        this.viewer = a;
        this.stripData = a.stripData;
        a = this.container = document.createElement("div");
        a.id = "marmosetUI";
        a.style.position = "absolute";
        a.style.overflow = "hidden";
        a.style["-moz-user-select"] = "none";
        a.style["-khtml-user-select"] = "none";
        a.style["-webkit-user-select"] = "none";
        a.style["-ms-user-select"] = "none";
        this.viewer.domRoot.appendChild(a)
    }
    UI.prototype.setSize = function(a, b) {
        this.container.width = a | 0;
        this.container.height = b | 0;
        this.container.style.width = a + "px";
        this.container.style.height = b + "px"
    };
    UI.prototype.clearView = function() {
        for (; this.container.hasChildNodes();) this.container.removeChild(this.container.childNodes[0]);
        delete this.progressBar;
        delete this.thumbnail;
        delete this.fadeThumbnail;
        delete this.playButton;
        delete this.helpOverlay
    };
    UI.prototype.bindInput = function(a) {
        a.onSingleTap.push(function(b, c) {
            this.stripData.selectedStrip != this.stripData.STRIP_NONE && (b = 2 / a.element.clientWidth * b - 1, c = 1 - 2 / a.element.clientHeight * c, this.stripData.selectStrip(b, c), this.stripData.selectedStrip == this.stripData.STRIP_MENU && this.helpOverlay.active && this.helpOverlay.toggle(), this.refreshUI(), this.viewer.wake())
        }.bind(this));
        a.onDoubleTap.push(function(a, c) {
            this.viewer.scene.view.reset();
            this.viewer.wake()
        }.bind(this))
    };
    UI.sanitize = function(a) {
        return a ? a.replace(/<|>|\(|\)|$|%|=/g, "") : a
    };
    UI.sanitizeURL = function(a) {
        return a ? 0 == a.indexOf("http://") || 0 == a.indexOf("https://") || 0 == a.indexOf("ftp://") ? encodeURI(a) : "http://" + encodeURI(a) : a
    };
    UI.prototype.showFailure = function(a) {
        this.container.innerHTML = '<br><br><br><p style="text-align:center;color:#aaaaaa"><b>Marmoset Viewer could not initialize.</b><br><i>' + (a || "") + "</i>"
    };
    UI.prototype.showPreview = function(a) {
        this.clearView();
        this.thumbnail = document.createElement("canvas");
        var b = this.container.width / this.container.height;
        this.thumbnail.height = 100;
        this.thumbnail.width = this.thumbnail.height * b | 0;
        this.thumbnail.style.width = this.thumbnail.style.height = "100%";
        var b = this.thumbnail.getContext("2d"),
            c = b.fillStyle = b.createRadialGradient(this.thumbnail.width / 2, this.thumbnail.height / 2, (this.thumbnail.width + this.thumbnail.height) / 2, this.thumbnail.width / 2, 0, 0);
        c.addColorStop(0, "rgb(0,0,0)");
        c.addColorStop(1, "rgb(150,150,150)");
        b.fillStyle = c;
        b.fillRect(0, 0, this.thumbnail.width, this.thumbnail.height);
        this.container.appendChild(this.thumbnail);
        this.playButton = document.createElement("input");
        this.playButton.type = "image";
        this.playButton.src = marmoset.dataLocale + "play.png";
        this.playButton.style.position = "absolute";
        this.playButton.style.left = "50%";
        this.playButton.style.top = "50%";
        this.playButton.style["-webkit-transform"] = this.playButton.style.transform = "translate(-50%,-50%) scale(0.5,0.5)";
        this.playButton.style.opacity = 0.5;
        this.playButton.style.outline = "0px";
        this.playButton.onclick = function() {
            this.viewer.loadScene(this.viewer.sceneURL);
            this.container.removeChild(this.playButton);
            delete this.playButton
        }.bind(this);
        this.container.appendChild(this.playButton);
        a || fetchThumbnail(this.viewer.sceneURL, function(a) {
            this.loadingImageURL || this.setThumbnail(a)
        }.bind(this))
    };
    UI.prototype.setThumbnailURL = function(a) {
        (this.loadingImageURL = a) && Network.fetchImage(this.loadingImageURL, this.setThumbnail.bind(this))
    };
    UI.prototype.setThumbnail = function(a) {
        if (this.thumbnail) {
            var b = this.thumbnail.getContext("2d"),
                c = this.thumbnail.width,
                d = this.thumbnail.height,
                e = d / a.height;
            b.drawImage(a, (c - a.width * e) / 2, 0, a.width * e, d);
            var f;
            try {
                f = b.getImageData(0, 0, c, d)
            } catch (g) {
                return
            }
            a = b.createImageData(c, d);
            for (e = 0; 3 > e; ++e) {
                for (var h = f.data, k = a.data, l = 0, m = 0; m < d; ++m)
                    for (var n = 0; n < c; ++n) {
                        for (var r = 0, p = 0, q = 0, u = -2; 2 >= u; ++u)
                            for (var s = m + u, s = 0 > s ? 0 : s >= d ? d - 1 : s, z = -2; 2 >= z; ++z) var t = n + z,
                                t = 0 > t ? 0 : t >= c ? c - 1 : t,
                                t = 4 * (s * c + t),
                                r = r + h[t],
                                p = p + h[t + 1],
                                q =
                                q + h[t + 2];
                        k[l++] = r / 25;
                        k[l++] = p / 25;
                        k[l++] = q / 25;
                        k[l++] = 255
                    }
                h = f;
                f = a;
                a = h
            }
            b.putImageData(f, 0, 0)
        }
    };
    UI.prototype.showActiveView = function() {
        var a = this.thumbnail;
        this.clearView();
        a && (this.fadeThumbnail = a, this.fadeThumbnail.style.opacity = 1, this.container.appendChild(this.fadeThumbnail));
        void 0 === marmoset.largeUI && (marmoset.largeUI = this.viewer.mobile);
        450 > this.container.widh && (marmoset.largeUI = !1);
        var b = FullScreen.support(),
            b = !0,
            a = 1;
        window.devicePixelRatio && (2 < window.devicePixelRatio ? a = 4 : 1 < window.devicePixelRatio && (a = 2));
        marmoset.largeUI && 4 > a && (a *= 2);
        var c = marmoset.largeUI ? 0.3 : 0.5;
        this.stripText = [];
        for (var d = 0; d < this.stripData.labels.length; ++d) {
            this.stripText[d] = document.createElement("div");
            this.stripText[d].style.position = "absolute";
            this.stripText[d].style.cursor = "pointer";
            this.stripText[d].style.pointerEvents = "none";
            this.container.appendChild(this.stripText[d]);
            var e = document.createElement("div");
            e.style.color = "white";
            e.style.opacity = 0.5;
            e.style.fontFamily = "Arial";
            e.style.textShadow = "2px 2px 3px #000000";
            e.innerHTML = this.stripData.labels[d];
            this.stripText[d].appendChild(e);
            this.stripText[d].txt =
                e;
            e = document.createElement("div");
            e.style.width = "10000px";
            e.style.height = "2px";
            e.style.backgroundColor = "#AAAAAA";
            e.style.opacity = 1;
            e.style.position = "absolute";
            e.style.left = e.style.top = "-1px";
            this.stripText[d].appendChild(e);
            this.stripText[d].line = e
        }
        this.sigCluster = document.createElement("div");
        this.sigCluster.style.position = "absolute";
        this.sigCluster.style.right = marmoset.largeUI ? "12px" : "9px";
        this.sigCluster.style.left = "0px";
        this.sigCluster.style.top = "6px";
        this.sigCluster.style.height = marmoset.largeUI ?
            "64px" : "32px";
        this.logo = document.createElement("div");
        this.logo.style.position = "absolute";
        this.logo.style.right = marmoset.largeUI ? "-4px" : "1px";
        this.logo.style.top = marmoset.largeUI ? "0px" : "4px";
        this.logo.title = "Made with Marmoset Toolbag";
        var f = document.createElement("input");
        f.type = "image";
        f.src = marmoset.dataLocale + "logo" + a + "x.png";
        f.style.border = "none";
        f.style.width = f.style.height = marmoset.largeUI ? "72px" : "36px";
        f.style.border = "0px";
        f.style.outline = "0px";
        f.style.opacity = c;
        f.style.display = "none"
        f.onmouseover = function() {
            this.style.opacity =
                1
        }.bind(f);
        f.onmouseout = function() {
            this.style.opacity = c
        }.bind(f);
        f.onclick = function(a) {
            a.menuCluster.toggle();
            a.helpOverlay.active && a.helpOverlay.toggle();
            a.refreshUI();
            this.style.opacity = c;
            this.blur()
        }.bind(f, this);
        d = new XMLHttpRequest;
        d.open("HEAD", f.src, !0);
        d.onload = function(a) {
            this.logo.appendChild(a)
        }.bind(this, f);
        d.send();
        this.sigCluster.appendChild(this.logo);
        d = this.viewer.scene.metaData;
        d.title = UI.sanitize(d.title);
        d.subtitle = UI.sanitize(d.subtitle);
        d.author = UI.sanitize(d.author);
        d.link = UI.sanitizeURL(d.link);
        var g = d.title && 0 < d.title.length,
            e = d.subtitle && 0 < d.subtitle.length,
            f = d.author && 0 < d.author.length,
            h = d.link && 0 < d.link.length;
        if (g || e || f) {
            g || (d.title = "Art");
            var k = !g && !e,
                l = document.createElement("div");
            l.style.position = "absolute";
            l.style.right = marmoset.largeUI ? "74px" : "46px";
            l.style.top = "5px";
            l.style.width = "1px";
            l.style.height = marmoset.largeUI ? k ? "21px" : "35px" : k ? "18px" : "31px";
            l.style.opacity = 0.25;
            l.style.backgroundColor = "white";
            this.sigCluster.appendChild(l);
            this.sigCluster.line = l;
            k = document.createElement("a");
            h && (k.href = d.link);
            k.style.position = "absolute";
            k.style.right = marmoset.largeUI ? "86px" : "58px";
            k.style.top = "6px";
            k.style.textAlign = "right";
            k.style.color = "white";
            k.style.fontFamily = "Arial";
            k.style.fontSize = marmoset.largeUI ? "14px" : "12px";
            k.style.textDecoration = "none";
            k.target = "_blank";
            l = document.createElement("font");
            l.style.color = "#FFFFFF";
            l.style.opacity = 0.5;
            l.style.textDecoration = "none";
            l.style.textShadow = "1px 1px 2px rgba(0,0,0,0.7)";
            l.innerHTML = d.title;
            f && (l.innerHTML = g && !e ? l.innerHTML + "<br>by " :
                l.innerHTML + " by ");
            k.appendChild(l);
            g = document.createElement("font");
            g.style.color = "#FF0044";
            g.style.opacity = 1;
            g.style.textShadow = "1px 1px 2px rgba(0,0,0,0.35)";
            g.innerHTML = d.author;
            k.appendChild(g);
            f = document.createElement("font");
            f.style.color = "#FFFFFF";
            f.style.opacity = 0.5;
            f.style.textShadow = "1px 1px 2px rgba(0,0,0,0.7)";
            e && (f.innerHTML = "<br>", f.innerHTML += d.subtitle);
            k.appendChild(f);
            h && (k.onmouseover = function(a, b, c) {
                a.style.opacity = c.style.opacity = 1;
                b.style.textDecoration = "underline"
            }.bind(k,
                l, g, f), k.onmouseout = function(a, b, c) {
                a.style.opacity = c.style.opacity = 0.5;
                b.style.textDecoration = "none"
            }.bind(k, l, g, f));
            this.sigCluster.appendChild(k);
            this.sigCluster.sceneTitle = k
        }
        this.container.appendChild(this.sigCluster);
        this.sigCluster.active = !0;
        this.sigCluster.toggle = function() {
            this.sceneTitle && this.line && (this.active ? (this.removeChild(this.sceneTitle), this.removeChild(this.line)) : (this.appendChild(this.sceneTitle), this.appendChild(this.line)));
            this.active = !this.active
        }.bind(this.sigCluster);
        this.helpOverlay =
            document.createElement("div");
        this.helpOverlay.style.pointerEvents = "none";
        this.container.appendChild(this.helpOverlay);
        this.hideSigOnHelp = d = 450 > this.container.width;
        this.hideSigOnStrips = !0;
        g = [8, 8];
        d ? (e = 198 + 2 * g[0], f = 258 + 2 * g[1]) : (e = 354 + 2 * g[0], f = 218 + 2 * g[1]);
        h = document.createElement("div");
        h.style.position = "absolute";
        h.style.width = h.style.height = "100%";
        this.helpOverlay.contents = h;
        h = document.createElement("div");
        h.style.position = "absolute";
        h.style.right = marmoset.largeUI ? "92px" : "54px";
        h.style.top = d ? "16px" :
            "48px";
        h.style.width = e + "px";
        h.style.height = f + "px";
        this.helpOverlay.contents.appendChild(h);
        f = document.createElement("div");
        f.style.position = "absolute";
        f.style.width = "100%";
        f.style.height = "100%";
        f.style.backgroundColor = "black";
        f.style.opacity = "0.65";
        f.style.borderRadius = "16px";
        h.appendChild(f);
        f = document.createElement("input");
        f.type = "button";
        f.value = "x";
        f.style.position = "absolute";
        f.style.color = "#FFFFFF";
        f.style.fontWeight = "bolder";
        f.style.backgroundColor = "rgba(0,0,0,0.0)";
        f.style.border = "0px";
        f.style.outline =
            "0px";
        f.style.fontSize = marmoset.largeUI ? "16pt" : "10pt";
        f.style.right = marmoset.largeUI ? "2px" : "8px";
        f.style.top = marmoset.largeUI ? "0px" : "4px";
        f.style.width = f.style.height = marmoset.largeUI ? "32px" : "16px";
        f.style.pointerEvents = "auto";
        f.style.cursor = "pointer";
        f.onclick = function(a) {
            this.helpOverlay.toggle();
            this.refreshUI();
            a.blur()
        }.bind(this, f);
        h.appendChild(f);
        f = document.createElement("center");
        f.style.position = "absolute";
        f.style.left = g[0] - 4 + "px";
        f.style.right = g[0] + 4 + "px";
        f.style.top = f.style.bottom = g[1] +
            "px";
        f.style.paddingTop = "8px";
        d || (f.style.paddingRight = "8px");
        h.appendChild(f);
        h = f;
        g = (this.viewer.mobile ? "M" : "PC") + (2 < a ? 4 : 2) + "x.png";
        f = document.createElement("img");
        f.src = marmoset.dataLocale + "helprotate" + g;
        f.style.width = "66px";
        f.style.height = "90px";
        h.appendChild(f);
        f = document.createElement("img");
        f.src = marmoset.dataLocale + "helpzoom" + g;
        f.style.width = "66px";
        f.style.height = "90px";
        h.appendChild(f);
        f = document.createElement("img");
        f.src = marmoset.dataLocale + "helpmove" + g;
        f.style.width = "66px";
        f.style.height =
            "90px";
        h.appendChild(f);
        f = document.createElement("img");
        f.src = marmoset.dataLocale + "helpreset" + g;
        f.style.width = "66px";
        f.style.height = "90px";
        h.appendChild(f);
        f = document.createElement("img");
        f.src = marmoset.dataLocale + "helplights" + g;
        f.style.position = "relative";
        d || (f.style.left = "8px");
        f.style.width = "66px";
        f.style.height = "90px";
        h.appendChild(f);
        g = document.createElement("a");
        g.href = "http://www.marmoset.co/viewer?utm_source=inapp&utm_medium=menu&utm_campaign=viewer";
        g.target = "_blank";
        g.style.pointerEvents =
            "auto";
        h.appendChild(g);
        k = document.createElement("img");
        k.src = marmoset.dataLocale + "helpshadow.png";
        k.style.position = "absolute";
        k.style.left = 0.5 * e - (d ? 65 : 116) + "px";
        k.style.bottom = d ? "6px" : "8px";
        k.style.width = d ? "116px" : "232px";
        k.style.opacity = 0;
        g.appendChild(k);
        k.targetOpacity = 0;
        g.onmouseover = function() {
            this.targetOpacity = 0.65
        }.bind(k);
        g.onmouseout = function() {
            this.targetOpacity = 0
        }.bind(k);
        window.setInterval(function() {
            this.style.opacity = 0.1 * this.targetOpacity + 0.9 * this.style.opacity
        }.bind(k), 20);
        f = document.createElement("img");
        f.src = marmoset.dataLocale + "helptitle.png";
        f.style.position = "absolute";
        f.style.left = 0.5 * e - (d ? 65 : 116) + "px";
        f.style.bottom = d ? "8px" : "12px";
        f.style.width = d ? "116px" : "232px";
        g.appendChild(f);
        e = document.createElement("div");
        e.style.position = "absolute";
        e.style.left = 0;
        e.style.right = d ? "30px" : "92px";
        e.style.bottom = d ? "-4px" : "4px";
        e.style.textAlign = "right";
        e.style.fontFamilly = "Arial";
        h.appendChild(e);
        d = document.createElement("font");
        d.style.fontSize = "9pt";
        d.style.fontFamily = "Arial";
        e.appendChild(d);
        g = document.createElement("a");
        g.style.color = "#FF0044";
        g.style.textDecoration = "none";
        g.style.pointerEvents = "auto";
        g.innerHTML = "www.marmoset.co/viewer";
        g.href = "http://www.marmoset.co/viewer?utm_source=inapp&utm_medium=menu&utm_campaign=viewer";
        g.target = "_blank";
        g.onmouseover = function(a) {
            this.style.textDecoration = "underline";
            a.targetOpacity = 0.65
        }.bind(g, k);
        g.onmouseout = function(a) {
            this.style.textDecoration = "none";
            a.targetOpacity = 0
        }.bind(g, k);
        d.appendChild(g);
        this.helpOverlay.active = !1;
        this.helpOverlay.toggle = function(a) {
            this.active ?
                this.removeChild(this.contents) : this.appendChild(this.contents);
            this.active = !this.active
        }.bind(this.helpOverlay, this.viewer);
        this.menuCluster = document.createElement("div");
        this.menuCluster.style.position = "absolute";
        this.menuCluster.style.right = marmoset.largeUI ? "4px" : "25px";
        this.menuCluster.style.top = marmoset.largeUI ? "70px" : "125px";
        /*marmoset.largeUI ? (this.menuCluster.style.width = "72px", this.menuCluster.style.height = "64px") : (this.menuCluster.style.width = "36px", this.menuCluster.style.height = "36px");*/
        h = document.createElement("div");
        h.style.left = h.style.top = "0px";
        h.style.width = h.style.height = "100%";
        this.menuCluster.contents = h;
        this.menuCluster.appendChild(h);
        d = 0;
        e = function(a, b, c, d, e) {
            var f = document.createElement("input");
            f.type = "image";
            f.src = marmoset.dataLocale + c;
/*            f.style.position = "absolute";
            f.style.left = "0px";
            f.style.bottom = -100 * d + "%";
            f.style.border = "none";
            f.style.outline = "0px";*/
            f.style.color = "rgb(66, 175, 250)";
            f.style.borderRadius = "15%";
            f.style.border = "2px solid rgb(66, 175, 250)";
            f.style.display = "block";
            f.style.opacity = "0.5";
            f.style.width = "70px";
            f.style.height = "40px";
            f.style.background = "rgba(0, 0, 0, 0.498039)";
            f.style.marginBottom = "8px";

            f.title = b;
            /*f.style.opacity = e;*/
            /*marmoset.largeUI ? (f.style.width = "64px", f.style.height = "48px") : (f.style.width = "32px", f.style.height = "24px");*/
            f.onmouseover = function(a) {
                this.style.opacity =
                    a
            }.bind(f, 1);
            f.onmouseout = function(a) {
                this.style.opacity = a
            }.bind(f, e);
            f.onmouseup = function(a) {
                this.style.opacity = a
            }.bind(f, e);
            b = new XMLHttpRequest;
            b.open("HEAD", f.src, !0);
            b.onload = function(a) {
                a.appendChild(this)
            }.bind(f, a);
            b.send();
            return f
        };
/*        b && (b = e(this.menuCluster.contents, "Full Screen", "fullscreen" + a + "x.png", d++, c), b.onclick = function(a) {
            FullScreen.active() ? FullScreen.end() : FullScreen.begin(this.viewer.domRoot, this.viewer.fullscreenChange.bind(this.viewer));
            a.style.opacity = c;
            this.refreshUI();
            a.blur()
        }.bind(this,
            b));*/
        b = e(this.menuCluster.contents, "Layer Views", "strips" + a + "x.png", d++, c);
        b.onclick = function(a) {
            this.stripData.toggleMenu();
            this.helpOverlay.active && this.helpOverlay.toggle();
            this.viewer.wake();
            this.refreshUI();
            a.blur()
            $j('.navHint').css('display','none');

        }.bind(this, b);
        b = e(this.menuCluster.contents, "Help", "help" + a + "x.png", d++, c);
        b.onclick = function(a) {
            this.stripData.selectedStrip == this.stripData.STRIP_MENU && this.stripData.toggleMenu();
            this.helpOverlay.toggle();
            this.refreshUI();
            a.blur()
        }.bind(this, b);
        this.container.appendChild(this.menuCluster);
        this.menuCluster.active = !0;
        this.menuCluster.toggle = function() {
            this.active ? this.removeChild(this.contents) : this.appendChild(this.contents);
            this.active = !this.active
        }.bind(this.menuCluster);
        void 0 !== marmoset.hostImage && (marmoset.hostURL && (g = document.createElement("a"), g.href = marmoset.hostURL, g.target = "_blank"), f = document.createElement("img"), f.src = marmoset.hostImage, f.style.position = "absolute", f.style.top = "4px", f.style.left = "4px", f.style.opacity = 0.65, f.style["-webkit-transform"] = f.style.transform = "translate(-50%,-50%) scale(0.5,0.5) translate(50%,50%)",
            marmoset.hostURL ? (f.onmouseover = function() {
                this.style.opacity = 1
            }.bind(f), f.onmouseout = function() {
                this.style.opacity = 0.5
            }.bind(f), g.appendChild(f), this.hostLogo = g) : this.hostLogo = f, d = new XMLHttpRequest, d.open("HEAD", f.src, !0), d.onload = function() {
                this.container.appendChild(this.hostLogo)
            }.bind(this), d.send());
        this.sceneStats = document.createElement("text");
        this.sceneStats.style.position = "absolute";
        this.sceneStats.style.left = "9px";
        this.sceneStats.style.bottom = "65px";
        this.sceneStats.style.color = "gray";
        this.sceneStats.style.fontFamily =
            "Arial";
        this.sceneStats.style.fontSize = "75%";
        for (d = b = a = 0; d < this.viewer.scene.meshes.length; ++d) e = this.viewer.scene.meshes[d], a += e.indexCount / 3, b += e.vertexCount;
        this.sceneStats.innerHTML = "Triangles: " + (a | 0).toLocaleString() + "<br>Vertices: " + (b | 0).toLocaleString();
        marmoset.showFrameTime && (this.frameTimer = document.createElement("text"), this.frameTimer.style.position = "absolute", this.frameTimer.style.left = this.frameTimer.style.top = "5px", this.frameTimer.style.color = "gray", this.frameTimer.style.fontSize =
            "75%", this.container.appendChild(this.frameTimer), this.frameTimer.innerHTML = "--", this.frameCount = 1E20);
        this.animateStrips()
    };
    UI.prototype.refreshUI = function() {
        if (this.sigCluster) {
            var a = !1,
                b = this.stripData.selectedStrip == this.stripData.STRIP_MENU;
            this.hideSigOnStrips && (a = a || b);
            this.hideSigOnHelp && (a = a || this.helpOverlay.active);
            this.sigCluster.active == a && this.sigCluster.toggle()
            $j('.navHint').css('display','');
        }
    };
    UI.prototype.signalLoadProgress = function(a, b) {
        if (this.thumbnail) {
            if (!this.progressBar) {
                var c = document.createElement("div");
                c.style.backgroundColor = "rgb(30,30,30)";
                c.style.opacity = 0.5;
                c.style.position = "absolute";
                c.style.left = "20%";
                c.style.width = "60%";
                c.style.bottom = "30%";
                c.style.height = "2px";
                this.progressBar = document.createElement("div");
                this.progressBar.style.backgroundColor = "white";
                this.progressBar.style.position = "absolute";
                this.progressBar.style.left = this.progressBar.style.bottom = "0px";
                this.progressBar.style.height =
                    "100%";
                this.progressBar.style.width = "0px";
                c.appendChild(this.progressBar);
                this.container.appendChild(c);
                this.playButton && (this.container.removeChild(this.playButton), delete this.playButton)
            }
            this.progressBar.style.width = 0 >= b ? (100 * a / (2097152 + a) | 0) + "%" : (100 * a / b | 0) + "%"
        }
    };
    UI.prototype.animating = function() {
        return !!this.fadeThumbnail || !!this.frameTimer
    };
    UI.prototype.animate = function() {
        this.fadeThumbnail && (this.fadeThumbnailTimer = this.fadeThumbnailTimer || Date.now(), this.fadeThumbnail.style.opacity = 1 - 0.0015 * (Date.now() - this.fadeThumbnailTimer), 0.01 > this.fadeThumbnail.style.opacity && (this.container.removeChild(this.fadeThumbnail), delete this.fadeThumbnail, delete this.fadeThumbnailTimer));
        if (this.frameTimer && (this.frameCount++, 60 <= this.frameCount)) {
            var a = (new Date).getTime();
            if (void 0 !== this.frameTime) {
                var b = (a - this.frameTime) / this.frameCount,
                    b = Math.floor(100 *
                        b) / 100;
                this.frameTimer.innerHTML = b + " ms";
                this.frameTimer.style.color = 32 > b ? "green" : "red"
            }
            this.frameCount = 0;
            this.frameTime = a
        }
        this.sceneStats && (a = !!this.sceneStats.parentElement, b = this.stripData.active(), a && !b ? (this.container.removeChild(this.sceneStats), this.hostLogo && this.container.appendChild(this.hostLogo)) : !a && b && (this.container.appendChild(this.sceneStats), this.hostLogo && this.container.removeChild(this.hostLogo)));
        this.refreshUI();
        this.stripData.animationActive && this.animateStrips()
    };
    UI.prototype.animateStrips = function() {
        if (this.stripText)
            for (var a = Math.atan(this.viewer.canvas.height / this.viewer.canvas.width / this.stripData.stripSlant), b = 0; b < this.stripData.labels.length; ++b) {
                var c = this.stripData.strips[b],
                    c = c - this.stripData.stripSlant,
                    c = 0.5 + 0.5 * c;
                b == this.stripData.selectedStrip ? (this.stripText[b].style["-ms-transform"] = this.stripText[b].style["-webkit-transform"] = this.stripText[b].style.transform = "none", this.stripText[b].style.top = "4px", this.stripText[b].style.left = "0px", this.stripText[b].style.width =
                    "150px", this.stripText[b].txt.style.textAlign = "center", this.stripText[b].txt.style.background = "rgba(0, 0, 0, 0.75)", this.stripText[b].txt.style.background = "-webkit-linear-gradient(left, rgba(0,0,0,0.75), rgba(0,0,0,0))", this.stripText[b].txt.style.background = "-o-linear-gradient(left,      rgba(0,0,0,0.75), rgba(0,0,0,0))", this.stripText[b].txt.style.background = "-moz-linear-gradient(left,    rgba(0,0,0,0.75), rgba(0,0,0,0))", this.stripText[b].txt.style.background = "linear-gradient(left,         rgba(0,0,0,0.75), rgba(0,0,0,0))",
                    this.stripText[b].txt.style.paddingLeft = "32px", this.stripText[b].txt.style.paddingTop = "6px", this.stripText[b].txt.style.paddingBottom = "4px", this.stripText[b].txt.style.textShadow = "1px 1px 2px rgba(0,0,0,0.7)", this.stripText[b].line.style.opacity = 0.5, this.stripText[b].line.style.top = "100%", this.stripText[b].line.style.width = "100%", this.stripText[b].line.style.height = "1px") : (this.stripText[b].style["-ms-transform"] = this.stripText[b].style["-webkit-transform"] = this.stripText[b].style.transform = "translate(-50%, -50%) rotate(" +
                    a + "rad) translate(50%, 50%)", this.stripText[b].style.left = 100 * c + "%", this.stripText[b].style.top = "0px", this.stripText[b].style.width = "85px", this.stripText[b].txt.style.textAlign = "left", this.stripText[b].txt.style.background = "none", this.stripText[b].txt.style.paddingLeft = "8px", this.stripText[b].txt.style.paddingTop = "6px", this.stripText[b].txt.style.paddingBottom = "4px", this.stripText[b].txt.style.textShadow = "2px 0px 3px rgba(0,0,0,0.7)", this.stripText[b].line.style.opacity = 1, this.stripText[b].line.style.top =
                    "-1px", this.stripText[b].line.style.width = "10000px", this.stripText[b].line.style.height = "2px")
            }
    };
    var Vect = {
        type: Float32Array,
        create: function(a, b, c, d) {
            var e = new Vect.type(4);
            e[0] = a;
            e[1] = b;
            e[2] = c;
            e[3] = d;
            return e
        },
        empty: function() {
            return new Vect.type(4)
        },
        set: function(a, b, c, d, e) {
            a[0] = b;
            a[1] = c;
            a[2] = d;
            a[3] = e
        },
        copy: function(a, b) {
            a[0] = b[0];
            a[1] = b[1];
            a[2] = b[2];
            a[3] = b[3]
        },
        add: function(a, b, c) {
            a[0] = b[0] + c[0];
            a[1] = b[1] + c[1];
            a[2] = b[2] + c[2];
            a[3] = b[3] + c[3];
            return a
        },
        sub: function(a, b, c) {
            a[0] = b[0] - c[0];
            a[1] = b[1] - c[1];
            a[2] = b[2] - c[2];
            a[3] = b[3] - c[3];
            return a
        },
        scale: function(a, b, c) {
            a[0] = c[0] * b;
            a[1] = c[1] * b;
            a[2] = c[2] *
                b;
            a[3] = c[3] * b;
            return a
        },
        mul: function(a, b, c) {
            a[0] = b[0] * c[0];
            a[1] = b[1] * c[1];
            a[2] = b[2] * c[2];
            a[3] = b[3] * c[3];
            return a
        },
        mad: function(a, b, c, d) {
            a[0] = b[0] * c[0] + d[0];
            a[1] = b[1] * c[1] + d[1];
            a[2] = b[2] * c[2] + d[2];
            a[3] = b[3] * c[3] + d[3];
            return a
        },
        smad: function(a, b, c, d) {
            a[0] = b * c[0] + d[0];
            a[1] = b * c[1] + d[1];
            a[2] = b * c[2] + d[2];
            a[3] = b * c[3] + d[3];
            return a
        },
        negate: function(a, b) {
            a[0] = -b[0];
            a[1] = -b[1];
            a[2] = -b[2];
            return a
        },
        negate4: function(a, b) {
            a[0] = -b[0];
            a[1] = -b[1];
            a[2] = -b[2];
            a[3] = -b[3];
            return a
        },
        length: function(a) {
            var b = a[0],
                c = a[1];
            a = a[2];
            return Math.sqrt(b * b + c * c + a * a)
        },
        dot: function(a, b) {
            return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
        },
        dot4: function(a, b) {
            return a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]
        },
        normalize: function(a, b) {
            var c = b[0],
                d = b[1],
                e = b[2],
                f = Math.sqrt(c * c + d * d + e * e);
            if (0 == f) return Vect.set(a, 0, 0, 0, 0);
            f = 1 / f;
            a[0] = c * f;
            a[1] = d * f;
            a[2] = e * f;
            return a
        },
        cross: function(a, b, c) {
            a[0] = b[1] * c[2];
            a[0] += -b[2] * c[1];
            a[1] = b[2] * c[0] - b[0] * c[2];
            a[2] = b[0] * c[1] - b[1] * c[0];
            return a
        },
        lerp: function(a, b, c, d) {
            var e = 1 - d;
            a[0] = b[0] * e + c[0] * d;
            a[1] = b[1] * e + c[1] * d;
            a[2] =
                b[2] * e + c[2] * d;
            return a
        },
        lerp4: function(a, b, c, d) {
            var e = 1 - d;
            a[0] = b[0] * e + c[0] * d;
            a[1] = b[1] * e + c[1] * d;
            a[2] = b[2] * e + c[2] * d;
            a[3] = b[3] * e + c[3] * d;
            return a
        },
        min: function(a, b, c) {
            a[0] = Math.min(b[0], c[0]);
            a[1] = Math.min(b[1], c[1]);
            a[2] = Math.min(b[2], c[2]);
            a[3] = Math.min(b[3], c[3]);
            return a
        },
        max: function(a, b, c) {
            a[0] = Math.max(b[0], c[0]);
            a[1] = Math.max(b[1], c[1]);
            a[2] = Math.max(b[2], c[2]);
            a[3] = Math.max(b[3], c[3]);
            return a
        },
        projectOnPlane: function(a, b, c, d) {
            var e = Vect.empty();
            Vect.sub(e, b, c);
            c = Vect.dot(e, d);
            smad(a, -c, normal,
                b);
            return a
        }
    };

    function View(a) {
        this.pivot = [0, 0, 0];
        this.rotation = [0, 0];
        this.radius = 1;
        this.nearPlane = 0.3;
        this.fov = 45;
        this.size = [1, 1];
        this.transform = Matrix.empty();
        this.viewMatrix = Matrix.empty();
        this.projectionMatrix = Matrix.empty();
        this.viewProjectionMatrix = Matrix.empty();
        this.projectionOffset = [0, 0];
        a ? this.loadView(a, !0) : (this.saveResetView(), this.updateView(), this.updateProjection())
    }
    View.prototype.saveResetView = function() {
        this.resetDesc = {
            angles: [this.rotation[0], this.rotation[1]],
            pivot: [this.pivot[0], this.pivot[1], this.pivot[2]],
            limits: this.limits,
            orbitRadius: this.radius,
            fov: this.fov
        }
    };
    View.prototype.loadView = function(a, b) {
        a && (this.rotation[0] = a.angles[0], this.rotation[1] = a.angles[1], this.pivot[0] = a.pivot[0], this.pivot[1] = a.pivot[1], this.pivot[2] = a.pivot[2], this.radius = a.orbitRadius, this.fov = a.fov, this.limits = a.limits, b && this.saveResetView(), this.updateView(), this.updateProjection())
    };
    View.prototype.reset = function() {
        this.loadView(this.resetDesc)
    };
    View.prototype.updateView = function() {
        if (void 0 !== this.limits) {
            if (this.limits.angles) {
                var a = this.limits.angles.x,
                    b = this.limits.angles.y;
                if (void 0 !== a) {
                    var c = this.rotation[0] - a.offset,
                        a = Math.min(Math.max(c, a.min), a.max);
                    this.rotation[0] += a - c
                }
                void 0 !== b && (c = this.rotation[1] - b.offset, a = Math.min(Math.max(c, b.min), b.max), this.rotation[1] += a - c)
            }
            void 0 !== this.limits.orbitRadius && (b = this.limits.orbitRadius.min, c = this.limits.orbitRadius.max, void 0 !== b && (this.radius = Math.max(this.radius, b)), void 0 !== c && (this.radius =
                Math.min(this.radius, c)));
            void 0 !== this.limits.pan && (b = this.limits.pan, c = this.resetDesc.pivot, b.x && (this.pivot[0] = c[0]), b.y && (this.pivot[1] = c[1]), b.z && (this.pivot[2] = c[2]))
        }
        Matrix.translation(this.transform, 0, 0, this.radius);
        b = Matrix.rotation(Matrix.empty(), this.rotation[0], 0);
        c = Matrix.rotation(Matrix.empty(), this.rotation[1], 1);
        Matrix.mul(b, c, b);
        Matrix.mul(this.transform, b, this.transform);
        this.transform[12] += this.pivot[0];
        this.transform[13] += this.pivot[1];
        this.transform[14] += this.pivot[2];
        Matrix.invert(this.viewMatrix,
            this.transform);
        Matrix.mul(this.viewProjectionMatrix, this.viewMatrix, this.projectionMatrix)
    };
    View.prototype.offsetProjection = function(a, b) {
        this.projectionOffset[0] = -2 * a;
        this.projectionOffset[1] = -2 * b
    };
    View.prototype.updateProjection = function(a) {
        Matrix.perspectiveInfinite(this.projectionMatrix, this.fov, this.size[0] / this.size[1], this.nearPlane, a);
        this.projectionMatrix[8] = this.projectionOffset[0];
        this.projectionMatrix[9] = this.projectionOffset[1];
        Matrix.mul(this.viewProjectionMatrix, this.projectionMatrix, this.viewMatrix)
    };

    function WebViewer(a, b, c, d) {
        this.mobile = /Android|iPhone|iPod|iPad|Windows Phone|IEMobile|BlackBerry|webOS/.test(navigator.userAgent);
        this.domRoot = document.createElement("div");
        this.domRoot.style.width = a + "px";
        this.domRoot.style.height = b + "px";
        this.initCanvas(a, b);
        this.scene = this.input = null;
        this.sceneURL = c;
        this.sleepCounter = 8;
        this.onLoad = null;
        this.stripData = new StripData;
        this.ui = new UI(this);
        this.ui.setSize(a, b);
        this.ui.showPreview(d)
    }
    WebViewer.prototype.initCanvas = function(a, b) {
        this.canvas && this.canvas.parentNode && this.canvas.parentNode.removeChild(this.canvas);
        this.canvas = document.createElement("canvas");
        this.canvas.width = 1 * a;
        this.canvas.height = 1 * b;
        this.canvas.style.width = a + "px";
        this.canvas.style.height = b + "px";
        this.canvas.style.position = "absolute";
        this.domRoot.appendChild(this.canvas)
    };
    WebViewer.prototype.initGL = function() {
        var a = {
                alpha: !1,
                depth: !1,
                stencil: !1,
                antialias: !1,
                premultipliedAlpha: !1,
                preserveDrawingBuffer: !1
            },
            a = this.gl = this.canvas.getContext("webgl", a) || this.canvas.getContext("experimental-webgl", a);
        if (!this.gl) return this.ui.showFailure('Please <a href="http://get.webgl.org/" target=_blank>check<a/> to ensure your browser has support for WebGL.'), !1;
        this.canvas.addEventListener("webglcontextlost", function(a) {
            a.preventDefault()
        }.bind(this), !1);
        this.canvas.addEventListener("webglcontextrestored",
            function(a) {
                this.loadScene(this.sceneURL)
            }.bind(this), !1);
        a.ext = {
            textureAniso: a.getExtension("EXT_texture_filter_anisotropic") || a.getExtension("WEBKIT_EXT_texture_filter_anisotropic") || a.getExtension("MOZ_EXT_texture_filter_anisotropic"),
            textureFloat: a.getExtension("OES_texture_float"),
            textureFloatLinear: a.getExtension("OES_texture_float_linear"),
            textureHalf: a.getExtension("OES_texture_half_float"),
            textureHalfLinear: a.getExtension("OES_texture_half_float_linear"),
            textureDepth: a.getExtension("WEBGL_depth_texture"),
            colorBufferFloat: a.getExtension("WEBGL_color_buffer_float"),
            colorBufferHalf: a.getExtension("EXT_color_buffer_half_float"),
            index32bit: a.getExtension("OES_element_index_uint"),
            loseContext: a.getExtension("WEBGL_lose_context"),
            derivatives: a.getExtension("OES_standard_derivatives")
        };
        a.limits = {
            textureSize: a.getParameter(a.MAX_TEXTURE_SIZE),
            varyings: a.getParameter(a.MAX_VARYING_VECTORS),
            vertexAttribs: a.getParameter(a.MAX_VERTEX_ATTRIBS),
            vertexUniforms: a.getParameter(a.MAX_VERTEX_UNIFORM_VECTORS),
            fragmentUniforms: a.getParameter(a.MAX_FRAGMENT_UNIFORM_VECTORS),
            viewportSizes: a.getParameter(a.MAX_VIEWPORT_DIMS),
            vendor: a.getParameter(a.VENDOR),
            version: a.getParameter(a.VERSION)
        };
        a.hints = {
            mobile: this.mobile
        };
        a.enable(a.DEPTH_TEST);
        a.shaderCache = new ShaderCache(a);
        a.textureCache = new TextureCache(a);
        this.allocBacking();
        return !0
    };
    WebViewer.prototype.allocBacking = function() {
        var a = this.gl,
            b = !1,
            c = {
                width: this.canvas.width,
                height: this.canvas.height
            };
        this.mainColor = new Texture(a, c);
        a.ext.textureHalf && a.ext.textureHalfLinear && (this.mainColor.loadArray(null, a.RGBA, a.ext.textureHalf.HALF_FLOAT_OES), this.mainBuffer = new Framebuffer(a, {
            color0: this.mainColor,
            createDepth: !0
        }), b = this.mainBuffer.valid);
        !b && a.ext.textureFloat && a.ext.textureFloatLinear && !a.hints.mobile && (this.mainColor.loadArray(null, a.RGBA, a.FLOAT), this.mainBuffer = new Framebuffer(a, {
            color0: this.mainColor,
            createDepth: !0
        }), b = this.mainBuffer.valid);
        for (; !b;) this.mainColor = new Texture(a, c), this.mainColor.loadArray(null, a.RGBA, a.UNSIGNED_BYTE), this.mainBuffer = new Framebuffer(a, {
            color0: this.mainColor,
            createDepth: !0
        }), b = this.mainBuffer.valid, c.width /= 2, c.height /= 2
    };
    WebViewer.prototype.loadScene = function(a) {
        this.sceneURL = a || this.sceneURL;
        this.scene = this.input = null;
        if (this.initGL() && this.sceneURL) {
            var b = this.ui.signalLoadProgress.bind(this.ui);
            a = function(a) {
                b(1, 1);
                this.scene = new Scene(this.gl);
                this.scene.stripData = this.stripData;
                if (this.scene.load(new Archive(a)))
                    if (2070 >= this.scene.metaData.tbVersion) this.ui.showFailure("This .mview file is from an out-of-date beta version of Toolbag. Please re-export it with the new version. Thanks!");
                    else {
                        if (this.bindInput(),
                            this.requestFrame(this.updateLoad.bind(this)), this.onLoad) this.onLoad()
                    } else this.ui.showFailure("Package file could not be read or is invalid.")
            }.bind(this);
            var c = function() {
                this.ui.showFailure("Package file (" + this.sceneURL + ") could not be retrieved.")
            }.bind(this);
            Network.fetchBinary(this.sceneURL, a, c, b)
        }
    };
    WebViewer.prototype.unload = function() {
        delete this.scene;
        delete this.input;
        delete this.ui;
        delete this.mainColor;
        delete this.mainBuffer;
        delete this.gl;
        var a = this.domRoot.clientWidth,
            b = this.domRoot.clientHeight;
        this.initCanvas(a, b);
        this.ui = new UI(this);
        this.ui.setSize(a, b);
        this.ui.showPreview();
        this.cancelFrame()
    };
    WebViewer.prototype.bindInput = function() {
        this.input = new Input(this.ui.container);
        var a = function() {
            this.wake();
            this.scene.postRender.discardAAHistory()
        }.bind(this);
        this.input.onDrag.push(function(b, c, d, e) {
            b = 1 - 2.2 / (Math.sqrt(d * d + e * e) + 2.2);
            c = this.scene.view;
            c.rotation[1] -= 0.4 * d * b;
            c.rotation[0] -= 0.4 * e * b;
            c.rotation[0] = 90 < c.rotation[0] ? 90 : c.rotation[0];
            c.rotation[0] = -90 > c.rotation[0] ? -90 : c.rotation[0];
            c.updateView();
            a()
        }.bind(this));
        this.input.onPan.push(function(b, c) {
            var d = this.scene.view,
                e = d.fov / 45 * 0.8 *
                (d.radius / this.domRoot.clientHeight),
                f = -b * e,
                e = c * e;
            d.pivot[0] += f * d.transform[0] + e * d.transform[4];
            d.pivot[1] += f * d.transform[1] + e * d.transform[5];
            d.pivot[2] += f * d.transform[2] + e * d.transform[6];
            d.updateView();
            a()
        }.bind(this));
        this.input.onPan2.push(function(b, c) {
            var d = 1 - 2.2 / (Math.sqrt(b * b + c * c) + 2.2);
            this.scene.lights.rotation -= 0.4 * b * d;
            a()
        }.bind(this));
        this.input.onZoom.push(function(b) {
            var c = this.scene.view;
            c.radius *= 1 - 0.002 * b;
            c.radius = 0.001 > c.radius ? 0.001 : c.radius;
            c.radius = 1E3 < c.radius ? 1E3 : c.radius;
            c.updateView();
            a()
        }.bind(this));
        this.ui.bindInput(this.input)
    };
    WebViewer.prototype.wake = function(a) {
        this.sleepCounter = a || 16;
        this.requestFrame(this.update.bind(this))
    };
    WebViewer.prototype.requestFrame = function(a) {
        var b = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;
        if (!this.frameRequestPending) {
            var c = function() {
                this.frameRequestPending = 0;
                a()
            }.bind(this);
            this.frameRequestPending = b(c, this.canvas)
        }
    };
    WebViewer.prototype.cancelFrame = function() {
        this.frameRequestPending && (window.cancelAnimationFrame || window.mozCancelAnimationFrame || window.webkitCancelAnimationFrame || window.msCancelAnimationFrame)(this.frameRequestPending)
    };
    WebViewer.prototype.fullscreenChange = function() {
        FullScreen.active() ? (this.oldRootWidth = this.domRoot.style.width, this.oldRootHeight = this.domRoot.style.height, this.domRoot.style.width = "100%", this.domRoot.style.height = "100%") : (this.domRoot.style.width = this.oldRootWidth, this.domRoot.style.height = this.oldRootHeight);
        this.wake()
    };
    WebViewer.prototype.resize = function(a, b) {
        a && b ? (this.domRoot.style.width = a + "px", this.domRoot.style.height = b + "px") : (a = this.domRoot.clientWidth, b = this.domRoot.clientHeight);
        this.canvas.width = 1 * a;
        this.canvas.height = 1 * b;
        this.canvas.style.width = a + "px";
        this.canvas.style.height = b + "px";
        this.ui.setSize(a, b);
        this.allocBacking();
        this.wake()
    };
    WebViewer.prototype.updateLoad = function() {
        this.scene.complete() ? this.start() : this.requestFrame(this.updateLoad.bind(this));
        this.ui.animate()
    };
    WebViewer.prototype.start = function() {
        this.scene.view.updateView();
        this.ui.showActiveView();
        this.requestFrame(this.update.bind(this))
    };
    WebViewer.prototype.update = function() {
        if (0 < this.sleepCounter || this.ui.animating() || this.stripData.animationActive) this.stripData.update(), this.ui.animate(), this.scene.update(), this.drawScene(), this.requestFrame(this.update.bind(this));
        this.sleepCounter--
    };
    WebViewer.prototype.drawScene = function() {
        this.gl.isContextLost() || (this.domRoot.clientWidth == this.canvas.clientWidth && this.domRoot.clientHeight == this.canvas.clientHeight || this.resize(), this.scene.view.size = [this.mainBuffer.width, this.mainBuffer.height], this.scene.view.updateProjection(), this.scene.postRender.adjustProjectionForSupersampling(this.scene.view), this.scene.collectShadows(this.mainBuffer), this.mainBuffer.bind(), this.scene.draw(), this.scene.postRender.present(this.mainColor, this.canvas.width,
            this.canvas.height, this.stripData.active()))
    };
    marmoset = "undefined" == typeof marmoset ? {} : marmoset;
    marmoset.WebViewer = WebViewer;
    var hosturl = window.location.host;
    marmoset.dataLocale = (0 == window.location.protocol.indexOf("https") ? "https:" : "http:") + "//" + hosturl + "/assets/scripts/marmoset/";
    /*marmoset.dataLocale == "http://" + hostname + "/assets/scripts/marmoset/";*/
    var ShaderTable = {
        "aaresolve.glsl": "precision mediump float;uniform sampler2D tInput0;uniform sampler2D tInput1;uniform sampler2D tInput2;\n#ifdef HIGHQ\nuniform sampler2D tInput3;\n#endif\nuniform vec4 uSamplesValid;varying highp vec2 d;void main(void){vec3 e=texture2D(tInput0,d).xyz;vec3 f=texture2D(tInput1,d).xyz;vec3 h=texture2D(tInput2,d).xyz;\n#ifdef HIGHQ\nvec3 i=texture2D(tInput3,d).xyz;gl_FragColor.xyz=e*uSamplesValid.x+f*uSamplesValid.y+h*uSamplesValid.z+i*uSamplesValid.w;\n#else\ngl_FragColor.xyz=e*uSamplesValid.x+f*uSamplesValid.y+h*uSamplesValid.z;\n#endif\ngl_FragColor.w=1.0;}",
        "alphaprepassfrag.glsl": "precision mediump float;\n#include <matdither.glsl>\nuniform sampler2D tAlbedo;varying mediump vec2 j;void main(){float k=texture2D(tAlbedo,j).a;if(k<=l(j.x)){discard;}gl_FragColor=vec4(0.0);}",
        "alphaprepassvert.glsl": "precision highp float;uniform mat4 uModelViewProjectionMatrix;attribute vec3 vPosition;attribute vec2 vTexCoord;varying mediump vec2 j;vec4 m(mat4 o,vec3 p){return o[0]*p.x+(o[1]*p.y+(o[2]*p.z+o[3]));}void main(void){gl_Position=m(uModelViewProjectionMatrix,vPosition.xyz);j=vTexCoord;}",
        "bloom.glsl": "precision mediump float;uniform sampler2D tInput;uniform vec4 uKernel[BLOOM_SAMPLES];varying highp vec2 d;void main(void){vec3 c=vec3(0.0,0.0,0.0);for(int u=0;u<BLOOM_SAMPLES;++u){vec3 v=uKernel[u].xyz;c+=texture2D(tInput,d+v.xy).xyz*v.z;}gl_FragColor.xyz=c;gl_FragColor.w=0.0;}",
        "bloomshrink.glsl": "precision highp float;uniform sampler2D tInput;varying highp vec2 d;void main(void){float A=0.25/256.0;gl_FragColor=0.25*(texture2D(tInput,d+vec2(A,A))+texture2D(tInput,d+vec2(A,-A))+texture2D(tInput,d+vec2(-A,A))+texture2D(tInput,d+vec2(-A,-A)));}",
        "matdither.glsl": "float l(highp float B){highp float C=0.5*fract(gl_FragCoord.x*0.5)+0.5*fract(gl_FragCoord.y*0.5);return 0.4+0.6*fract(C+3.141592e6*B);}",
        "matfrag.glsl": "\n#extension GL_OES_standard_derivatives : enable\nprecision mediump float;varying highp vec3 D;varying mediump vec2 j;varying mediump vec3 E;varying mediump vec3 F;varying mediump vec3 G;\n#ifdef VERTEX_COLOR\nvarying lowp vec4 H;\n#endif\n#ifdef TEXCOORD_SECONDARY\nvarying mediump vec2 I;\n#endif\nuniform sampler2D tAlbedo;uniform sampler2D tReflectivity;uniform sampler2D tNormal;uniform sampler2D tExtras;uniform sampler2D tSkySpecular;uniform vec4 uDiffuseCoefficients[9];uniform vec3 uCameraPosition;uniform vec3 uFresnel;uniform float uAlphaTest;uniform float uHorizonOcclude;uniform float uHorizonSmoothing;\n#ifdef EMISSIVE\nuniform float uEmissiveScale;uniform vec4 uTexRangeEmissive;\n#endif\n#ifdef AMBIENT_OCCLUSION\nuniform vec4 uTexRangeAO;\n#endif\n#ifdef LIGHT_COUNT\nuniform vec4 uLightPositions[LIGHT_COUNT];uniform vec3 uLightDirections[LIGHT_COUNT];uniform vec3 uLightColors[LIGHT_COUNT];uniform vec3 uLightParams[LIGHT_COUNT];uniform vec3 uLightSpot[LIGHT_COUNT];\n#endif\n#ifdef ANISO\nuniform float uAnisoStrength;uniform vec3 uAnisoTangent;uniform float uAnisoIntegral;uniform vec4 uTexRangeAniso;\n#endif\n#define saturate(x) clamp( x, 0.0, 1.0 )\n#include <matsampling.glsl>\n#include <matlighting.glsl>\n#include <matshadows.glsl>\n#include <matskin.glsl>\n#include <matmicrofiber.glsl>\n#include <matstrips.glsl>\n#ifdef TRANSPARENCY_DITHER\n#include <matdither.glsl>\n#endif\nvoid main(void){vec4 J=texture2D(tAlbedo,j);vec3 K=L(J.xyz);float k=J.w;\n#ifdef VERTEX_COLOR\n{vec3 M=H.xyz;\n#ifdef VERTEX_COLOR_SRGB\nM=M*(M*(M*0.305306011+vec3(0.682171111))+vec3(0.012522878));\n#endif\nK*=M;\n#ifdef VERTEX_COLOR_ALPHA\nk*=H.w;\n#endif\n}\n#endif\n#ifdef ALPHA_TEST\nif(k<uAlphaTest){discard;}\n#endif\n#ifdef TRANSPARENCY_DITHER\nk=(k>l(j.x))?1.0:k;\n#endif\nvec3 N=O(texture2D(tNormal,j).xyz);\n#ifdef ANISO\n#ifdef ANISO_NO_DIR_TEX\nvec3 P=Q(uAnisoTangent);\n#else\nJ=R(j,uTexRangeAniso);vec3 P=2.0*J.xyz-vec3(1.0);P=Q(P);\n#endif\nP=P-N*dot(P,N);P=normalize(P);vec3 S=P*uAnisoStrength;\n#endif\nvec3 T=normalize(uCameraPosition-D);J=texture2D(tReflectivity,j);vec3 U=L(J.xyz);float V=J.w;float W=V;\n#ifdef HORIZON_SMOOTHING\nfloat X=dot(T,N);X=uHorizonSmoothing-X*uHorizonSmoothing;V=mix(V,1.0,X*X);\n#endif\n#ifdef STRIPVIEW\nY Z;dc(Z,V,U);\n#endif\nfloat dd=1.0;\n#ifdef AMBIENT_OCCLUSION\n#ifdef AMBIENT_OCCLUSION_SECONDARY_UV\ndd=R(I,uTexRangeAO).x;\n#else\ndd=R(j,uTexRangeAO).x;\n#endif\ndd*=dd;\n#endif\n#if defined(SKIN)\nde df;dh(df);df.di*=dd;\n#elif defined(MICROFIBER)\ndj dk;dl(dk,N);dk.dm*=dd;\n#else\nvec3 dn=du(N);dn*=dd;\n#endif\nvec3 dv=reflect(-T,N);\n#ifdef ANISO\nvec3 rt=dv-(0.5*S*dot(dv,P));vec3 dA=dB(rt,mix(V,0.5*V,uAnisoStrength));\n#else\nvec3 dA=dB(dv,V);\n#endif\ndA*=dC(dv,G);\n#ifdef LIGHT_COUNT\nhighp float dD=10.0/log2(V*0.968+0.03);dD*=dD;float dE=dD*(1.0/(8.0*3.1415926))+(4.0/(8.0*3.1415926));dE=min(dE,1.0e3);\n#ifdef SHADOW_COUNT\ndF dG;dH(dG,SHADOW_KERNEL);\n#ifdef SKIN\ndF dI;dH(dI,SHADOW_KERNEL+SHADOW_KERNEL*df.dJ);\n#endif\n#endif\n#ifdef ANISO\ndE*=uAnisoIntegral;\n#endif\nfor(int u=0;u<LIGHT_COUNT;++u){vec3 dK=uLightPositions[u].xyz-D*uLightPositions[u].w;float dL=inversesqrt(dot(dK,dK));dK*=dL;float a=saturate(uLightParams[u].z/dL);a=1.0+a*(uLightParams[u].x+uLightParams[u].y*a);float s=saturate(dot(dK,uLightDirections[u]));s=saturate(uLightSpot[u].y-uLightSpot[u].z*(1.0-s*s));vec3 dM=(a*s)*uLightColors[u].xyz;\n#if defined(SKIN)\n#ifdef SHADOW_COUNT\ndN(df,dG.dO[u],dI.dO[u],dK,N,dM);\n#else\ndN(df,1.0,1.0,dK,N,dM);\n#endif\n#elif defined(MICROFIBER)\n#ifdef SHADOW_COUNT\ndP(dk,dG.dO[u],dK,N,dM);\n#else\ndP(dk,1.0,dK,N,dM);\n#endif\n#else\nfloat dQ=saturate((1.0/3.1415926)*dot(dK,N));\n#ifdef SHADOW_COUNT\ndQ*=dG.dO[u];\n#endif\ndn+=dQ*dM;\n#endif\nvec3 dR=dK+T;\n#ifdef ANISO\ndR=dR-(S*dot(dR,P));\n#endif\ndR=normalize(dR);float dS=dE*pow(saturate(dot(dR,N)),dD);\n#ifdef SHADOW_COUNT\ndS*=dG.dO[u];\n#endif\ndA+=dS*dM;}\n#endif\n#if defined(SKIN)\nvec3 dn,diff_extra;dT(dn,diff_extra,df,T,N,V);\n#elif defined(MICROFIBER)\nvec3 dn,diff_extra;dU(dn,diff_extra,dk,T,N,V);\n#endif\ndA*=dV(T,N,U,V*V);\n#ifdef DIFFUSE_UNLIT\ngl_FragColor.xyz=K+dA;\n#else\ngl_FragColor.xyz=dn*K+dA;\n#endif\n#if defined(SKIN) || defined(MICROFIBER)\ngl_FragColor.xyz+=diff_extra;\n#endif\n#ifdef EMISSIVE\n#ifdef EMISSIVE_SECONDARY_UV\nvec2 dW=I;\n#else\nvec2 dW=j;\n#endif\ngl_FragColor.xyz+=uEmissiveScale*L(R(dW,uTexRangeEmissive).xyz);\n#endif\n#ifdef STRIPVIEW\ngl_FragColor.xyz=dX(Z,N,K,U,W,dn,dA,gl_FragColor.xyz);\n#endif\ngl_FragColor.w=k;}",
        "matlighting.glsl": "float dY(float dZ,float ec){return saturate(-dZ*ec+dZ+ec);}vec3 ed(float dZ,vec3 ec){return saturate(-dZ*ec+vec3(dZ)+ec);}float ee(float ec){return-0.31830988618379*ec+0.31830988618379;}vec3 ef(vec3 ec){return-0.31830988618379*ec+vec3(0.31830988618379);}vec3 dV(vec3 T,vec3 N,vec3 U,float eh){float ei=1.0-saturate(dot(T,N));float ej=ei*ei;ei*=ej*ej;ei*=eh;return(U-ei*U)+ei*uFresnel;}vec2 ek(vec2 el,vec2 ec){el=1.0-el;vec2 em=el*el;em*=em;el=mix(em,el*0.4,ec);return el;}vec3 du(vec3 en){\n#define c(n) uDiffuseCoefficients[n].xyz\nvec3 C=(c(0)+en.y*((c(1)+c(4)*en.x)+c(5)*en.z))+en.x*(c(3)+c(7)*en.z)+c(2)*en.z;\n#undef c\nvec3 sqr=en*en;C+=uDiffuseCoefficients[6].xyz*(3.0*sqr.z-1.0);C+=uDiffuseCoefficients[8].xyz*(sqr.x-sqr.y);return C;}void eo(inout vec3 eu,inout vec3 ev,inout vec3 eA,vec3 en){eu=uDiffuseCoefficients[0].xyz;ev=uDiffuseCoefficients[1].xyz*en.y;ev+=uDiffuseCoefficients[2].xyz*en.z;ev+=uDiffuseCoefficients[3].xyz*en.x;vec3 swz=en.yyz*en.xzx;eA=uDiffuseCoefficients[4].xyz*swz.x;eA+=uDiffuseCoefficients[5].xyz*swz.y;eA+=uDiffuseCoefficients[7].xyz*swz.z;vec3 sqr=en*en;eA+=uDiffuseCoefficients[6].xyz*(3.0*sqr.z-1.0);eA+=uDiffuseCoefficients[8].xyz*(sqr.x-sqr.y);}vec3 eB(vec3 eu,vec3 ev,vec3 eA,vec3 eC,float ec){eC=mix(vec3(1.0),eC,ec);return(eu+ev*eC.x)+eA*eC.z;}vec3 eD(vec3 eu,vec3 ev,vec3 eA,vec3 eC,vec3 eE){vec3 eF=mix(vec3(1.0),eC.yyy,eE);vec3 eG=mix(vec3(1.0),eC.zzz,eE);return(eu+ev*eF)+eA*eG;}vec3 dB(vec3 en,float V){en/=dot(vec3(1.0),abs(en));vec2 eH=abs(en.zx)-vec2(1.0,1.0);vec2 eI=vec2(en.x<0.0?eH.x:-eH.x,en.z<0.0?eH.y:-eH.y);vec2 eJ=(en.y<0.0)?eI:en.xz;eJ=vec2(0.5*(254.0/256.0),0.125*0.5*(254.0/256.0))*eJ+vec2(0.5,0.125*0.5);float eK=fract(7.0*V);eJ.y+=0.125*(7.0*V-eK);vec2 eL=eJ+vec2(0.0,0.125);vec4 eM=mix(texture2D(tSkySpecular,eJ),texture2D(tSkySpecular,eL),eK);vec3 r=eM.xyz*(7.0*eM.w);return r*r;}float dC(vec3 en,vec3 eN){float eO=dot(en,eN);eO=saturate(1.0+uHorizonOcclude*eO);return eO*eO;}",
        "matmicrofiber.glsl": "\n#ifdef MICROFIBER\nuniform vec4 uTexRangeFuzz;uniform float uFresnelIntegral;uniform vec4 uFresnelColor;uniform float uFresnelOcc;uniform float uFresnelGlossMask;struct dj{vec3 dm;vec3 dQ;vec3 eP;vec3 eQ;vec3 eR;};void dl(out dj s,vec3 N){s.dm=s.dQ=du(N);s.eP=vec3(0.0);s.eQ=uFresnelColor.rgb;s.eR=uFresnelColor.aaa*vec3(1.0,0.5,0.25);\n#ifndef MICROFIBER_NO_FUZZ_TEX\nvec4 J=R(j,uTexRangeFuzz);s.eQ*=L(J.rgb);\n#endif\n}void dP(inout dj s,float eS,vec3 dK,vec3 N,vec3 dM){float dZ=dot(dK,N);float dQ=saturate((1.0/3.1415926)*dZ);float eT=dY(dZ,s.eR.z);\n#ifdef SHADOW_COUNT\ndQ*=eS;float eU=mix(1.0,eS,uFresnelOcc);float eP=eT*eU;\n#else \nfloat eP=eT;\n#endif\ns.eP=eP*dM+s.eP;s.dQ=dQ*dM+s.dQ;}void dU(out vec3 dn,out vec3 diff_extra,inout dj s,vec3 T,vec3 N,float V){s.eP*=uFresnelIntegral;float el=dot(T,N);vec2 eV=ek(vec2(el,el),s.eR.xy);s.eP=s.dm*eV.x+(s.eP*eV.y);s.eP*=s.eQ;float eW=saturate(1.0+-uFresnelGlossMask*V);s.eP*=eW*eW;dn=s.dQ;diff_extra=s.eP;}\n#endif\n",
        "matsampling.glsl": "vec3 L(vec3 c){return c*c;}vec3 O(vec3 n){vec3 eX=E;vec3 eY=F;vec3 eZ=gl_FrontFacing?G:-G;\n#ifdef TSPACE_RENORMALIZE\neZ=normalize(eZ);\n#endif\n#ifdef TSPACE_ORTHOGONALIZE\neX-=dot(eX,eZ)*eZ;\n#endif\n#ifdef TSPACE_RENORMALIZE\neX=normalize(eX);\n#endif\n#ifdef TSPACE_ORTHOGONALIZE\neY=(eY-dot(eY,eZ)*eZ)-dot(eY,eX)*eX;\n#endif\n#ifdef TSPACE_RENORMALIZE\neY=normalize(eY);\n#endif\n#ifdef TSPACE_COMPUTE_BITANGENT\nvec3 fc=cross(eZ,eX);eY=dot(fc,eY)<0.0?-fc:fc;\n#endif\nn=2.0*n-vec3(1.0);return normalize(eX*n.x+eY*n.y+eZ*n.z);}vec3 Q(vec3 t){vec3 eZ=gl_FrontFacing?G:-G;return normalize(E*t.x+F*t.y+eZ*t.z);}vec4 R(vec2 fd,vec4 fe){\n#if GL_OES_standard_derivatives\nvec2 ff=fract(fd);vec2 fh=fwidth(ff);float fi=(fh.x+fh.y)>0.5?-6.0:0.0;return texture2D(tExtras,ff*fe.xy+fe.zw,fi);\n#else\nreturn texture2D(tExtras,fract(fd)*fe.xy+fe.zw);\n#endif\n}vec3 fj(sampler2D fk,vec2 fl,float fm){vec3 n=texture2D(fk,fl,fm*4.0).xyz;return O(n);}",
        "matshadows.glsl": "\n#ifdef SHADOW_COUNT\n#ifdef MOBILE\n#define SHADOW_KERNEL (4.0/1536.0)\n#else\n#define SHADOW_KERNEL (4.0/2048.0)\n#endif\nhighp vec4 m(highp mat4 o,highp vec3 p){return o[0]*p.x+(o[1]*p.y+(o[2]*p.z+o[3]));}uniform sampler2D tDepth0;\n#if SHADOW_COUNT > 1\nuniform sampler2D tDepth1;\n#if SHADOW_COUNT > 2\nuniform sampler2D tDepth2;\n#endif\n#endif\nuniform highp vec2 uShadowKernelRotation;uniform highp vec4 uShadowMapSize;uniform highp mat4 uShadowMatrices[SHADOW_COUNT];uniform highp vec4 uShadowTexelPadProjections[SHADOW_COUNT];highp float fn(highp vec3 C){return(C.x+C.y*(1.0/255.0))+C.z*(1.0/65025.0);}float fo(sampler2D fu,highp vec2 fd,highp float fv){\n#ifndef MOBILE\nhighp vec2 c=fd*uShadowMapSize.xy;highp vec2 a=floor(c)*uShadowMapSize.zw,b=ceil(c)*uShadowMapSize.zw;vec4 fA;fA.x=fv<fn(texture2D(fu,a).xyz)?1.0:0.0;fA.y=fv<fn(texture2D(fu,vec2(b.x,a.y)).xyz)?1.0:0.0;fA.z=fv<fn(texture2D(fu,vec2(a.x,b.y)).xyz)?1.0:0.0;fA.w=fv<fn(texture2D(fu,b).xyz)?1.0:0.0;highp vec2 w=c-a*uShadowMapSize.xy;vec2 t=(w.y*fA.zw+fA.xy)-w.y*fA.xy;return(w.x*t.y+t.x)-w.x*t.x;\n#else\nhighp float C=fn(texture2D(fu,fd.xy).xyz);return fv<C?1.0:0.0;\n#endif\n}float fB(sampler2D fu,highp vec3 fd,float fC){highp vec2 v=uShadowKernelRotation*fC;float s;s=fo(fu,fd.xy+v,fd.z);s+=fo(fu,fd.xy-v,fd.z);s+=fo(fu,fd.xy+vec2(-v.y,v.x),fd.z);s+=fo(fu,fd.xy+vec2(v.y,-v.x),fd.z);s*=0.25;return s*s;}struct dF{float dO[LIGHT_COUNT];};void dH(out dF ss,float fC){highp vec3 fD[SHADOW_COUNT];vec3 eZ=gl_FrontFacing?G:-G;for(int u=0;u<SHADOW_COUNT;++u){vec4 fE=uShadowTexelPadProjections[u];float fF=fE.x*D.x+(fE.y*D.y+(fE.z*D.z+fE.w));\n#ifdef MOBILE\nfF*=.001+fC;\n#else\nfF*=.0005+0.5*fC;\n#endif\nhighp vec4 fG=m(uShadowMatrices[u],D+fF*eZ);fD[u]=fG.xyz/fG.w;}\n#if SHADOW_COUNT > 0\nss.dO[0]=fB(tDepth0,fD[0],fC);\n#endif\n#if SHADOW_COUNT > 1\nss.dO[1]=fB(tDepth1,fD[1],fC);\n#endif\n#if SHADOW_COUNT > 2\nss.dO[2]=fB(tDepth2,fD[2],fC);\n#endif\nfor(int u=SHADOW_COUNT;u<LIGHT_COUNT;++u){ss.dO[u]=1.0;}}\n#endif\n",
        "matskin.glsl": "\n#ifdef SKIN\nuniform vec4 uTexRangeSubdermis;uniform vec4 uTexRangeTranslucency;uniform vec4 uTexRangeFuzz;uniform vec3 uSubdermisColor;uniform vec4 uTransColor;uniform vec4 uFresnelColor;uniform float uFresnelOcc;uniform float uFresnelGlossMask;uniform float uTransSky;uniform float uFresnelIntegral;uniform float uTransIntegral;uniform float uSkinShadowBlur;uniform float uNormalSmooth;struct de{vec3 fH;vec3 fI,fJ,fK,eP;vec3 di,dm,fL;vec3 fM;vec3 fN;vec3 fO;vec3 fP;float fQ;float fR;float dJ;};void dh(out de s){vec4 J;\n#ifdef SKIN_NO_SUBDERMIS_TEX\ns.fH=uSubdermisColor;s.fR=1.0;\n#else \nJ=R(j,uTexRangeSubdermis);s.fH=L(J.xyz);s.fR=J.w*J.w;\n#endif\ns.fP=uTransColor.rgb;s.fQ=uTransColor.a;\n#ifndef SKIN_NO_TRANSLUCENCY_TEX\nJ=R(j,uTexRangeTranslucency);s.fP*=L(J.xyz);\n#endif\ns.fM=fj(tNormal,j,uNormalSmooth*s.fR);vec3 fS,fT,fU;eo(fS,fT,fU,s.fM);s.dm=s.fI=fS+fT+fU;s.di=eD(fS,fT,fU,vec3(1.0,0.6667,0.25),s.fH);vec3 fV,fW,fX;eo(fV,fW,fX,-s.fM);s.fL=eB(fV,fW,fX,vec3(1.0,0.4444,0.0625),s.fQ);s.fL*=uTransSky;s.fJ=s.fK=s.eP=vec3(0.0);s.dJ=uSkinShadowBlur*s.fR;s.fH*=0.5;s.fQ*=0.5;s.fN=uFresnelColor.rgb;s.fO=uFresnelColor.aaa*vec3(1.0,0.5,0.25);\n#ifndef SKIN_NO_FUZZ_TEX\nJ=R(j,uTexRangeFuzz);s.fN*=L(J.rgb);\n#endif\n}void dN(inout de s,float eS,float fY,vec3 dK,vec3 N,vec3 dM){float dZ=dot(dK,N);float fZ=dot(dK,s.fM);float dQ=saturate((1.0/3.1415926)*dZ);vec3 hc=ed(fZ,s.fH);float hd=dY(-fZ,s.fQ);vec3 fK=vec3(hd*hd);\n#ifdef SHADOW_COUNT\nfloat he=fY;vec3 hf=vec3(fY);float hh=saturate(eS-2.0*(fY*fY));hf+=hh*s.fH;\n#endif\nfloat eT=dY(fZ,s.fO.z);\n#ifdef SHADOW_COUNT\nvec3 eU=mix(vec3(1.0),hf,uFresnelOcc);vec3 eP=eT*eU;\n#else\nvec3 eP=vec3(eT);\n#endif\n#ifdef SHADOW_COUNT\nhc*=hf;fK*=he;dQ*=eS;\n#endif\ns.eP=eP*dM+s.eP;s.fK=fK*dM+s.fK;s.fJ=hc*dM+s.fJ;s.fI=dQ*dM+s.fI;}void dT(out vec3 dn,out vec3 diff_extra,inout de s,vec3 T,vec3 N,float V){s.eP*=uFresnelIntegral;float el=dot(T,N);vec2 eV=ek(vec2(el,el),s.fO.xy);s.eP=s.dm*eV.x+(s.eP*eV.y);s.eP*=s.fN;float eW=saturate(1.0+-uFresnelGlossMask*V);s.eP*=eW*eW;s.fJ=s.fJ*ef(s.fH)+s.di;s.fK=s.fK*uTransIntegral+s.fL;s.fK*=s.fP;dn=mix(s.fI,s.fJ,s.fR);diff_extra=(s.eP+s.fK)*s.fR;}\n#endif\n",
        "matstrips.glsl": "\n#ifdef STRIPVIEW\nuniform float uStrips[5];uniform vec2 uStripRes;struct Y{float hi[5];float bg;};void dc(out Y hj,inout float V,inout vec3 U){highp vec2 fd=gl_FragCoord.xy*uStripRes-vec2(1.0,1.0);fd.x+=0.25*fd.y;hj.hi[0]=step(fd.x,uStrips[0]);hj.hi[1]=step(fd.x,uStrips[1]);hj.hi[2]=step(fd.x,uStrips[2]);hj.hi[3]=step(fd.x,uStrips[3]);hj.hi[4]=step(fd.x,uStrips[4]);hj.bg=1.0-hj.hi[4];hj.hi[4]-=hj.hi[3];hj.hi[3]-=hj.hi[2];hj.hi[2]-=hj.hi[1];hj.hi[1]-=hj.hi[0];bool hk=hj.hi[4]>0.0;V=hk?0.5:V;U=hk?vec3(0.1):U;}vec3 dX(Y hj,vec3 N,vec3 K,vec3 U,float V,vec3 dn,vec3 dA,vec3 hl){return hj.hi[0]*(N*0.5+vec3(0.5))+hj.hi[1]*K+hj.hi[2]*U+vec3(hj.hi[3]*V)+hj.hi[4]*(vec3(0.12)+0.3*dn+dA)+hj.bg*hl;}\n#endif\n",
        "matvert.glsl": "precision highp float;uniform mat4 uModelViewProjectionMatrix;uniform mat4 uSkyMatrix;attribute vec3 vPosition;attribute vec2 vTexCoord;attribute vec2 vTangent;attribute vec2 vBitangent;attribute vec2 vNormal;\n#ifdef VERTEX_COLOR\nattribute vec4 vColor;\n#endif\n#ifdef TEXCOORD_SECONDARY\nattribute vec2 vTexCoord2;\n#endif\nvarying highp vec3 D;varying mediump vec2 j;varying mediump vec3 E;varying mediump vec3 F;varying mediump vec3 G;\n#ifdef VERTEX_COLOR\nvarying lowp vec4 H;\n#endif\n#ifdef TEXCOORD_SECONDARY\nvarying mediump vec2 I;\n#endif\nvec3 hm(vec2 hn){bool ho=(hn.y>(32767.1/65535.0));hn.y=ho?(hn.y-(32768.0/65535.0)):hn.y;vec3 r;r.xy=(2.0*65535.0/32767.0)*hn-vec2(1.0);r.z=sqrt(clamp(1.0-dot(r.xy,r.xy),0.0,1.0));r.z=ho?-r.z:r.z;return r;}vec4 m(mat4 o,vec3 p){return o[0]*p.x+(o[1]*p.y+(o[2]*p.z+o[3]));}vec3 hu(mat4 o,vec3 hn){return o[0].xyz*hn.x+o[1].xyz*hn.y+o[2].xyz*hn.z;}void main(void){gl_Position=m(uModelViewProjectionMatrix,vPosition.xyz);j=vTexCoord;E=hu(uSkyMatrix,hm(vTangent));F=hu(uSkyMatrix,hm(vBitangent));G=hu(uSkyMatrix,hm(vNormal));D=m(uSkyMatrix,vPosition.xyz).xyz;\n#ifdef VERTEX_COLOR\nH=vColor;\n#endif\n#ifdef TEXCOORD_SECONDARY\nI=vTexCoord2;\n#endif\n}",
        "postfrag.glsl": "precision mediump float;uniform sampler2D tInput;\n#ifdef BLOOM\nuniform sampler2D tBloom;\n#endif\n#ifdef GRAIN\nuniform sampler2D tGrain;\n#endif\n#ifdef COLOR_LUT\nuniform sampler2D tLUT;\n#endif\nuniform vec3 uScale;uniform vec3 uBias;uniform vec3 uSaturation;uniform vec4 uSharpenKernel;uniform vec3 uSharpness;uniform vec3 uBloomColor;uniform vec4 uVignetteAspect;uniform vec4 uVignette;uniform vec4 uGrainCoord;uniform vec2 uGrainScaleBias;varying vec2 d;vec3 hv(vec3 c){vec3 hA=sqrt(c);return(hA-hA*c)+c*(0.4672*c+vec3(0.5328));}void main(void){vec3 c=texture2D(tInput,d).xyz;\n#ifdef SHARPEN\nvec3 fA=texture2D(tInput,d+uSharpenKernel.xy).xyz;fA+=texture2D(tInput,d-uSharpenKernel.xy).xyz;fA+=texture2D(tInput,d+uSharpenKernel.zw).xyz;fA+=texture2D(tInput,d-uSharpenKernel.zw).xyz;vec3 hB=uSharpness.x*c-uSharpness.y*fA;c+=clamp(hB,-uSharpness.z,uSharpness.z);\n#endif\n#ifdef BLOOM\nc+=uBloomColor*texture2D(tBloom,d).xyz;\n#endif\n#ifdef VIGNETTE\nvec2 hC=d*uVignetteAspect.xy-uVignetteAspect.zw;vec3 hn=clamp(vec3(1.0,1.0,1.0)-uVignette.xyz*dot(hC,hC),0.0,1.0);vec3 hD=hn*hn;hD*=hn;c*=mix(hn,hD,uVignette.w);\n#endif\n#ifdef SATURATION\nfloat gray=dot(c,vec3(0.3,0.59,0.11));c=mix(vec3(gray,gray,gray),c,uSaturation);\n#endif\n#ifdef CONTRAST\nc=c*uScale+uBias;\n#endif\n#ifdef GRAIN\nfloat hE=uGrainScaleBias.x*texture2D(tGrain,d*uGrainCoord.xy+uGrainCoord.zw).x+uGrainScaleBias.y;c+=c*hE;\n#endif\n#ifdef REINHARD\n{c*=1.8;float hF=dot(c,vec3(0.3333));c=clamp(c/(1.0+hF),0.0,1.0);}\n#elif defined(HEJL)\n{const highp float hG=0.22,hH=0.3,hI=.1,hJ=0.2,hK=.01,hL=0.3;const highp float hM=1.25;highp vec3 dR=max(vec3(0.0),c-vec3(.004));c=(dR*((hM*hG)*dR+hM*vec3(hI*hH,hI*hH,hI*hH))+hM*vec3(hJ*hK,hJ*hK,hJ*hK))/(dR*(hG*dR+vec3(hH,hH,hH))+vec3(hJ*hL,hJ*hL,hJ*hL))-hM*vec3(hK/hL,hK/hL,hK/hL);}\n#endif\n#ifdef COLOR_LUT\nc=clamp(c,0.0,1.0);c=(255.0/256.0)*c+vec3(0.5/256.0);c.x=texture2D(tLUT,c.xx).x;c.y=texture2D(tLUT,c.yy).y;c.z=texture2D(tLUT,c.zz).z;c*=c;\n#endif\ngl_FragColor.xyz=hv(c);gl_FragColor.w=1.0;}",
        "postvert.glsl": "precision highp float;attribute vec2 vCoord;varying vec2 d;void main(void){d=vCoord;gl_Position.xy=2.0*vCoord-vec2(1.0,1.0);gl_Position.zw=vec2(0.0,1.0);}",
        "shadowfrag.glsl": "precision highp float;varying vec2 hN;\n#ifdef ALPHA_TEST\nvarying mediump vec2 j;uniform sampler2D tAlbedo;\n#endif\nvec3 hO(float hn){vec4 hP=vec4(1.0,255.0,65025.0,16581375.0)*hn;hP=fract(hP);hP.xyz-=hP.yzw*(1.0/255.0);return hP.xyz;}void main(void){\n#ifdef ALPHA_TEST\nfloat k=texture2D(tAlbedo,j).a;if(k<0.5){discard;}\n#endif\ngl_FragColor.xyz=hO((hN.x/hN.y)*0.5+0.5);gl_FragColor.w=0.0;}",
        "shadowvert.glsl": "precision highp float;attribute vec3 vPosition;attribute vec2 vTexCoord;uniform mat4 uViewProjection;varying vec2 hN;\n#ifdef ALPHA_TEST\nvarying mediump vec2 j;\n#endif\nvec4 m(mat4 o,vec3 p){return o[0]*p.x+(o[1]*p.y+(o[2]*p.z+o[3]));}void main(void){gl_Position=m(uViewProjection,vPosition);hN=gl_Position.zw;\n#ifdef ALPHA_TEST\nj=vTexCoord;\n#endif\n}",
        "sky.glsl": "precision highp float;uniform sampler2D tSkyTexture;uniform float uAlpha;varying vec2 j;void main(void){vec3 r=texture2D(tSkyTexture,j).xyz;gl_FragColor.xyz=r*r;gl_FragColor.w=uAlpha;}",
        "skySH.glsl": "precision mediump float;uniform vec4 uSkyCoefficients[9];uniform float uAlpha;varying vec3 hQ;void main(void){vec3 C=normalize(hQ);vec3 r=uSkyCoefficients[0].xyz;r+=uSkyCoefficients[1].xyz*C.y;r+=uSkyCoefficients[2].xyz*C.z;r+=uSkyCoefficients[3].xyz*C.x;vec3 swz=C.yyz*C.xzx;r+=uSkyCoefficients[4].xyz*swz.x;r+=uSkyCoefficients[5].xyz*swz.y;r+=uSkyCoefficients[7].xyz*swz.z;vec3 sqr=C*C;r+=uSkyCoefficients[6].xyz*(3.0*sqr.z-1.0);r+=uSkyCoefficients[8].xyz*(sqr.x-sqr.y);gl_FragColor.xyz=r;gl_FragColor.w=uAlpha;}",
        "skyvert.glsl": "precision highp float;uniform mat4 uInverseSkyMatrix;uniform mat4 uViewProjection;attribute vec3 vPosition;attribute vec2 vTexCoord;\n#if SKYMODE == 3\nvarying vec3 hQ;\n#else\nvarying vec2 j;\n#endif\nvec4 m(mat4 o,vec3 p){return o[0]*p.x+(o[1]*p.y+(o[2]*p.z+o[3]));}vec4 hu(mat4 o,vec3 hn){return o[0]*hn.x+o[1]*hn.y+o[2]*hn.z;}void main(void){vec3 p=m(uInverseSkyMatrix,vPosition).xyz;gl_Position=hu(uViewProjection,p);gl_Position.z-=(1.0/65535.0)*gl_Position.w;\n#if SKYMODE == 3\nhQ=vPosition;hQ.xy+=1e-20*vTexCoord;\n#else\nj=vTexCoord;\n#endif\n}",
        "wirefrag.glsl": "precision highp float;uniform vec4 uStripParams;void main(void){vec2 c=gl_FragCoord.xy*uStripParams.xy-vec2(1.0,1.0);c.x+=0.25*c.y;float a=c.x<uStripParams.z?0.0:0.9;a=c.x<uStripParams.w?a:0.0;gl_FragColor=vec4(0.0,0.0,0.0,a);}",
        "wirevert.glsl": "precision highp float;uniform mat4 uModelViewProjectionMatrix;attribute vec3 vPosition;vec4 m(mat4 o,vec3 p){return o[0]*p.x+(o[1]*p.y+(o[2]*p.z+o[3]));}void main(void){gl_Position=m(uModelViewProjectionMatrix,vPosition);gl_Position.z+=-0.00005*gl_Position.w;}",
        nil: ""
    };
})(marmoset);