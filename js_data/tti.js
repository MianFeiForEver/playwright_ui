(function() {
  'use strict';
(function() {
  /**
   * @return {undefined}
   */
  function error() {
    /**
     * @return {undefined}
     */
    error = function() {
    };
    if (!self.Symbol) {
      /** @type {function(string): ?} */
      self.Symbol = Symbol;
    }
  }
  /**
   * @param {string} name
   * @return {?}
   */
  function Symbol(name) {
    return "jscomp_symbol_" + (name || "") + n++;
  }
  /**
   * @return {undefined}
   */
  function polyfill() {
    error();
    var $iterator$ = self.Symbol.iterator;
    if (!$iterator$) {
      $iterator$ = self.Symbol.iterator = self.Symbol("iterator");
    }
    if ("function" != typeof Array.prototype[$iterator$]) {
      defineProperty(Array.prototype, $iterator$, {
        configurable : true,
        writable : true,
        value : function() {
          return find(this);
        }
      });
    }
    /**
     * @return {undefined}
     */
    polyfill = function() {
    };
  }
  /**
   * @param {string} b
   * @return {?}
   */
  function find(b) {
    /** @type {number} */
    var i = 0;
    return main(function() {
      return i < b.length ? {
        done : false,
        value : b[i++]
      } : {
        done : true
      };
    });
  }
  /**
   * @param {string} array
   * @return {?}
   */
  function main(array) {
    polyfill();
    array = {
      next : array
    };
    /**
     * @return {?}
     */
    array[self.Symbol.iterator] = function() {
      return this;
    };
    return array;
  }
  /**
   * @param {!Function} a
   * @return {?}
   */
  function push(a) {
    polyfill();
    var b = a[Symbol.iterator];
    return b ? b.call(a) : find(a);
  }
  /**
   * @param {!Object} result
   * @return {?}
   */
  function setup(result) {
    if (!(result instanceof Array)) {
      result = push(result);
      var _s;
      /** @type {!Array} */
      var _arr = [];
      for (; !(_s = result.next()).done;) {
        _arr.push(_s.value);
      }
      /** @type {!Array} */
      result = _arr;
    }
    return result;
  }
  /**
   * @param {?} callback
   * @param {?} responseFN
   * @return {undefined}
   */
  function injectAjaxInterceptor(callback, responseFN) {
    /** @type {function(this:XMLHttpRequest, (ArrayBuffer|ArrayBufferView|Blob|Document|FormData|null|string)=): undefined} */
    var oldSend = XMLHttpRequest.prototype.send;
    /** @type {number} */
    var thisBatch = batchId++;
    /**
     * @param {(ArrayBuffer|ArrayBufferView|Blob|Document|FormData|null|string)=} cmdBuffer
     * @return {undefined}
     */
    XMLHttpRequest.prototype.send = function(cmdBuffer) {
      /** @type {!Array} */
      var data = [];
      /** @type {number} */
      var i = 0;
      for (; i < arguments.length; ++i) {
        data[i - 0] = arguments[i];
      }
      /** @type {!XMLHttpRequest} */
      var checkusersrequest = this;
      callback(thisBatch);
      this.addEventListener("readystatechange", function() {
        if (4 === checkusersrequest.readyState) {
          responseFN(thisBatch);
        }
      });
      return oldSend.apply(this, data);
    };
  }
  /**
   * @param {?} fn
   * @param {?} b
   * @return {undefined}
   */
  function constructor(fn, b) {
    /** @type {function((Request|string), !RequestInit=): !Promise<Response>} */
    var fetchNonIdempotent = fetch;
    /**
     * @param {?} pagesInfoAndParameters
     * @return {?}
     */
    fetch = function(pagesInfoAndParameters) {
      /** @type {!Array} */
      var args = [];
      /** @type {number} */
      var i = 0;
      for (; i < arguments.length; ++i) {
        args[i - 0] = arguments[i];
      }
      return new Promise(function(saveNotifs, e) {
        /** @type {number} */
        var track = batchId++;
        fn(track);
        fetchNonIdempotent.apply(null, [].concat(setup(args))).then(function(notifications) {
          b(track);
          saveNotifs(notifications);
        }, function(applyBackgroundUpdates) {
          b(applyBackgroundUpdates);
          e(applyBackgroundUpdates);
        });
      });
    };
  }
  /**
   * @param {!Object} i
   * @param {string} b
   * @return {?}
   */
  function callback(i, b) {
    i = push(i);
    var child = i.next();
    for (; !child.done; child = i.next()) {
      if (child = child.value, b.includes(child.nodeName.toLowerCase()) || callback(child.children, b)) {
        return true;
      }
    }
    return false;
  }
  /**
   * @param {?} fcn
   * @return {?}
   */
  function on(fcn) {
    /** @type {!MutationObserver} */
    var observer = new MutationObserver(function(c) {
      c = push(c);
      var event = c.next();
      for (; !event.done; event = c.next()) {
        event = event.value;
        if ("childList" == event.type && callback(event.addedNodes, existingTables)) {
          fcn(event);
        } else {
          if ("attributes" == event.type && existingTables.includes(event.target.tagName.toLowerCase())) {
            fcn(event);
          }
        }
      }
    });
    observer.observe(document, {
      attributes : true,
      childList : true,
      subtree : true,
      attributeFilter : ["href", "src"]
    });
    return observer;
  }
  /**
   * @param {number} t
   * @param {number} i
   * @return {?}
   */
  function next(t, i) {
    if (2 < t.length) {
      return performance.now();
    }
    /** @type {!Array} */
    var self = [];
    i = push(i);
    var f = i.next();
    for (; !f.done; f = i.next()) {
      f = f.value;
      self.push({
        timestamp : f.start,
        type : "requestStart"
      });
      self.push({
        timestamp : f.end,
        type : "requestEnd"
      });
    }
    i = push(t);
    f = i.next();
    for (; !f.done; f = i.next()) {
      self.push({
        timestamp : f.value,
        type : "requestStart"
      });
    }
    self.sort(function(draftB, draftA) {
      return draftB.timestamp - draftA.timestamp;
    });
    t = t.length;
    /** @type {number} */
    i = self.length - 1;
    for (; 0 <= i; i--) {
      switch(f = self[i], f.type) {
        case "requestStart":
          t--;
          break;
        case "requestEnd":
          t++;
          if (2 < t) {
            return f.timestamp;
          }
          break;
        default:
          throw Error("Internal Error: This should never happen");
      }
    }
    return 0;
  }
  /**
   * @param {!Object} config
   * @return {undefined}
   */
  function init(config) {
    config = config ? config : {};
    /** @type {boolean} */
    this.w = !!config.useMutationObserver;
    this.u = config.minValue || null;
    config = window.__tti && window.__tti.e;
    var otherOutlet = window.__tti && window.__tti.o;
    this.a = config ? config.map(function(query) {
      return {
        start : query.startTime,
        end : query.startTime + query.duration
      };
    }) : [];
    if (otherOutlet) {
      otherOutlet.disconnect();
    }
    /** @type {!Array} */
    this.b = [];
    /** @type {!Map} */
    this.f = new Map;
    /** @type {null} */
    this.j = null;
    /** @type {number} */
    this.v = -Infinity;
    /** @type {boolean} */
    this.i = false;
    /** @type {null} */
    this.h = this.c = this.s = null;
    injectAjaxInterceptor(this.m.bind(this), this.l.bind(this));
    constructor(this.m.bind(this), this.l.bind(this));
    update(this);
    if (this.w) {
      this.h = on(this.B.bind(this));
    }
  }
  /**
   * @param {!Object} result
   * @return {undefined}
   */
  function k(result) {
    /** @type {boolean} */
    result.i = true;
    var f = 0 < result.a.length ? result.a[result.a.length - 1].end : 0;
    var len = next(result.g, result.b);
    test(result, Math.max(len + 5E3, f));
  }
  /**
   * @param {!Object} options
   * @param {number} date
   * @return {undefined}
   */
  function test(options, date) {
    if (!(!options.i || options.v > date)) {
      clearTimeout(options.j);
      /** @type {number} */
      options.j = setTimeout(function() {
        /** @type {number} */
        var undefined = performance.timing.navigationStart;
        var val = next(options.g, options.b);
        /** @type {number} */
        undefined = (window.a && window.a.A ? 1E3 * window.a.A().C - undefined : 0) || performance.timing.domContentLoadedEventEnd - undefined;
        if (options.u) {
          var t = options.u;
        } else {
          if (performance.timing.domContentLoadedEventEnd) {
            /** @type {!PerformanceTiming} */
            t = performance.timing;
            /** @type {number} */
            t = t.domContentLoadedEventEnd - t.navigationStart;
          } else {
            /** @type {null} */
            t = null;
          }
        }
        /** @type {number} */
        var z = performance.now();
        if (null === t) {
          test(options, Math.max(val + 5E3, z + 1E3));
        }
        var node = options.a;
        if (5E3 > z - val) {
          /** @type {null} */
          val = null;
        } else {
          val = node.length ? node[node.length - 1].end : undefined;
          /** @type {(null|number)} */
          val = 5E3 > z - val ? null : Math.max(val, t);
        }
        if (val) {
          options.s(val);
          clearTimeout(options.j);
          /** @type {boolean} */
          options.i = false;
          if (options.c) {
            options.c.disconnect();
          }
          if (options.h) {
            options.h.disconnect();
          }
        }
        test(options, performance.now() + 1E3);
      }, date - performance.now());
      /** @type {number} */
      options.v = date;
    }
  }
  /**
   * @param {!Object} self
   * @return {undefined}
   */
  function update(self) {
    /** @type {!PerformanceObserver} */
    self.c = new PerformanceObserver(function(list) {
      list = push(list.getEntries());
      var e = list.next();
      for (; !e.done; e = list.next()) {
        if (e = e.value, "resource" === e.entryType && (self.b.push({
          start : e.fetchStart,
          end : e.responseEnd
        }), test(self, next(self.g, self.b) + 5E3)), "longtask" === e.entryType) {
          var hashStart = e.startTime + e.duration;
          self.a.push({
            start : e.startTime,
            end : hashStart
          });
          test(self, hashStart + 5E3);
        }
      }
    });
    self.c.observe({
      entryTypes : ["longtask", "resource"]
    });
  }
  var self = "undefined" != typeof window && window === this ? this : "undefined" != typeof global && null != global ? global : this;
    self = window
  /** @type {!Function} */
  var defineProperty = "function" == typeof Object.defineProperties ? Object.defineProperty : function(object, name, descriptor) {
    if (object != Array.prototype && object != Object.prototype) {
      object[name] = descriptor.value;
    }
  };
  /** @type {number} */
  var n = 0;
  /** @type {number} */
  var batchId = 0;
  /** @type {!Array<string>} */
  var existingTables = "img script iframe link audio video source".split(" ");
  /**
   * @return {?}
   */
  init.prototype.getFirstConsistentlyInteractive = function() {
    var d = this;
    return new Promise(function(size) {
      d.s = size;
      if ("complete" == document.readyState) {
        k(d);
      } else {
        window.addEventListener("load", function() {
          k(d);
        });
      }
    });
  };
  /**
   * @param {?} input
   * @return {undefined}
   */
  init.prototype.m = function(input) {
    this.f.set(input, performance.now());
  };
  /**
   * @param {?} input
   * @return {undefined}
   */
  init.prototype.l = function(input) {
    this.f.delete(input);
  };
  /**
   * @return {undefined}
   */
  init.prototype.B = function() {
    test(this, performance.now() + 5E3);
  };
  self.Object.defineProperties(init.prototype, {
    g : {
      configurable : true,
      enumerable : true,
      get : function() {
        return [].concat(setup(this.f.values()));
      }
    }
  });
  var Phalanx = {
    getFirstConsistentlyInteractive : function(selector) {
      selector = selector ? selector : {};
      return "PerformanceLongTaskTiming" in window ? (new init(selector)).getFirstConsistentlyInteractive() : Promise.resolve(null);
    }
  };
  if ("undefined" != typeof module && module.exports) {
    module.exports = Phalanx;
  } else {
    if ("function" === typeof define && define.amd) {
      define("ttiPolyfill", [], function() {
        return Phalanx;
      });
    } else {
      window.ttiPolyfill = Phalanx;
    }
  }
})();
    ttiPolyfill.getFirstConsistentlyInteractive().then((tti) => {
        window.tti = tti
        console.log('tti..........',tti,'========获取tti========')

    });
})();