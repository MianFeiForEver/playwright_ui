(function () {


    class FPS {
        frames = 0;//当前frame

        NORMAL_FPS_THRESHOLDS = 55;// 无操作分界限
        FPS_COUNT = 3;// 连续几个则开始/结束
        SAMPLING = 100;// 每多少毫秒取一次帧率
        KEYCODE = 81;// 快捷键q
        BREAK_OFF_BOTH_ENDS = false;// frameList是否掐头去尾

        lowFpsCount = 0;
        normalFpsCount = 0;
        isStart = false;
        isStartCollect = false;
        isChecked = false;
        prevTime = 0;
        timepiece;
        timestemp = undefined;
        frameList = [];
        info = {}

        dom;
        button;
        span;
        div;

        constructor() {
            this.frameHandler = this.frameHandler.bind(this)
            this.prevTime = Date.now();
            this.dom = document.createElement('div');
            this.dom.style.position = 'absolute';
            this.dom.style.top = '0px';
            this.dom.style.left = '500px';
            this.dom.style.padding = '10px 20px';
            // this.dom.style.width = '200px'
            // this.dom.style.height = '100px'
            this.dom.style.color = '#fff';
            this.dom.style.background = '#A44D4D';
            this.dom.style.zIndex = '9999999';
            this.button = document.createElement('button');
            this.button.innerHTML = '开始'
            const _this = this
            this.button.addEventListener('click', this.clickEvent.bind(_this))
            window.addEventListener("keydown", function (event) {
                if (event.keyCode === _this.KEYCODE) {
                    _this.clickEvent.call(_this)
                }
            }, true);
            this.span = document.createElement('div');
            this.div = document.createElement('div');

            document.body.appendChild(this.dom);
            this.dom.appendChild(this.span);
            this.dom.appendChild(this.button);
            this.dom.appendChild(this.div);
            this.frameHandler();
        }

        frameHandler() {

            this.frames++;
            const time = Date.now();
            if (time >= this.prevTime + this.SAMPLING) {
                let fps = Math.round((this.frames * 1000) / (time - this.prevTime))
                if (fps > 60) {
                    fps = 60
                }

                this.span.innerHTML = fps;
                this.prevTime = time;
                this.frames = 0;
                if (this.isStart) {
                    if (this.BREAK_OFF_BOTH_ENDS) {
                        if (!this.isStartCollect) {
                            if (fps < this.NORMAL_FPS_THRESHOLDS) {
                                this.lowFpsCount += 1;
                            } else {
                                this.lowFpsCount = 0;
                            }
                            if (this.lowFpsCount >= this.FPS_COUNT) {
                                this.isStartCollect = true
                                this.timestemp = new Date();
                            }
                        } else {
                            this.frameList.push(fps)
                            if (fps > this.NORMAL_FPS_THRESHOLDS) {
                                this.normalFpsCount += 1;
                            } else {
                                this.normalFpsCount = 0
                            }
                            if (this.normalFpsCount >= this.FPS_COUNT) {
                                this.isChecked = false;
                                this.isStartCollect = false;
                                this.normalFpsCount = 0;
                                this.lowFpsCount = 0;
                                // 结束
                                this.clickEvent.call(this)
                            }
                        }
                    } else {
                        this.frameList.push(fps)
                    }
                }
            }
            requestAnimationFrame(this.frameHandler)
        }

        clickEvent() {
            if (!this.isStart) {
                this.isStart = true;
                if (!this.BREAK_OFF_BOTH_ENDS) {
                    this.timestemp = new Date();
                }
                this.button.innerHTML = '结束'
            } else {
                this.isStart = false;
                this.timepiece = new Date() - this.timestemp;
                this.timestemp = undefined;
                this.button.innerHTML = '开始'
                if (this.BREAK_OFF_BOTH_ENDS) {
                    if (this.frameList.length < 3) return
                    this.frameList.splice(this.frameList.length - 3, this.frameList.length - 1);
                }
                this.frameList.sort((a, b) => b - a)
                const p95 = this.frameList[Math.floor(this.frameList.length * 0.95)]
                const avg = (this.frameList.reduce(function (prev, curr, idx, arr) {
                    return prev + curr;
                }) / this.frameList.length).toFixed(2)
                const worst = this.frameList[this.frameList.length - 1]
                const vari = this.variance(this.frameList);
                const proportion = this.proportion(this.frameList)
                const str = `version:${window.LatestPackageVersion} \n buildTime:${window.LatestBuildTime} \n耗时：${this.timepiece};\nP95：${p95};\n平均帧率：${avg};\n最差帧率：${worst};\n方差：${vari};\n占比情况：${proportion}`;
                this.info['耗时'] = this.timepiece
                this.info['P95'] = p95
                this.info['平均帧率'] = avg
                this.info['最差帧率'] = worst
                this.info['方差'] = vari
                this.info['fps数据'] = this.frameList
                this.info['version'] = window.LatestPackageVersion
                this.info['buildTime'] = window.LatestBuildTime

                // console.debug(str);
                // console.debug('frameList end: ', this.frameList);
                // console.debug('info',this.info)
                console.debug(str);
                console.log('frameList end: ', this.frameList);
                console.log('info', this.info)
                // this.div.innerHTML = str
                this.frameList = []
                this.button.innerHTML = '开始'
            }
        }

        variance(arr) {
            var sum = 0;
            var s = 0;
            for (var i = 0; i < arr.length; i++) {
                sum += arr[i]
            }
            const ave = sum / arr.length;
            for (var j = 0; j < arr.length; j++) {
                s += Math.pow((ave - arr[j]), 2);
            }
            return Math.sqrt((s / arr.length), 2).toFixed(2);
            // 计算的方差不正确，改使用上面的方式 06.13  bjwuzh
            // // 计算方差
            // const total = arr.reduce(function (prev, curr, idx, arr) {
            //   return prev + curr;
            // });
            // const avg = total / arr.length
            // const squareAdd = arr.reduce(function (prev, curr, idx, arr) {
            //   const square = Math.pow(curr - avg, 2)
            //   return prev + square;
            // });
            // return (squareAdd / arr.length).toFixed(2)
        }

        proportion(arr) {
            // 计算占比
            const count = arr.length;

            let under_20 = 0;
            let twenty_to_thirty = 0;
            let thirty_to_forty = 0;
            let forty_to_fifty = 0;
            let more_then_fifty = 0;

            arr.map(item => {
                if (item <= 20)
                    under_20 += 1;
                else if (item <= 30)
                    twenty_to_thirty += 1;
                else if (item <= 40)
                    thirty_to_forty += 1;
                else if (item <= 50)
                    forty_to_fifty += 1;
                else
                    more_then_fifty += 1;
            })
            // const res = ` \n帧率在20以下的共计：${under_20}个，占比：${(under_20 / count * 100).toFixed(2)}%;\n20-30的共计：${twenty_to_thirty}个，占比：${(twenty_to_thirty / count * 100).toFixed(2)}%;\n30-40的共计：${thirty_to_forty}个，占比：${(thirty_to_forty / count * 100).toFixed(2)}%;\n40-50的共计：${forty_to_fifty}个，占比：${(forty_to_fifty / count * 100).toFixed(2)}%;\n50以上的共计：${more_then_fifty}个，占比：${(more_then_fifty / count * 100).toFixed(2)}%`
            // this.info['占比在20以下'] = (under_20 / count * 100).toFixed(2)+'%'
            // this.info['占比在20-30'] =(twenty_to_thirty / count * 100).toFixed(2)+'%'
            // this.info['占比在30-40'] = (thirty_to_forty / count * 100).toFixed(2)+'%'
            // this.info['占比在40-50'] =(forty_to_fifty / count * 100).toFixed(2)+'%'
            // this.info['占比在50以上'] = (more_then_fifty / count * 100).toFixed(2)+'%'
            const res = `\n帧率在20以下的共计：${under_20}个，占比：${(under_20 / count * 100).toFixed(2)};\n20-30的共计：${twenty_to_thirty}个，占比：${(twenty_to_thirty / count * 100).toFixed(2)};\n30-40的共计：${thirty_to_forty}个，占比：${(thirty_to_forty / count * 100).toFixed(2)};\n40-50的共计：${forty_to_fifty}个，占比：${(forty_to_fifty / count * 100).toFixed(2)};\n50以上的共计：${more_then_fifty}个，占比：${(more_then_fifty / count * 100).toFixed(2)}`
            this.info['占比在20以下'] = (under_20 / count * 100).toFixed(2)
            this.info['占比在20-30'] = (twenty_to_thirty / count * 100).toFixed(2)
            this.info['占比在30-40'] = (thirty_to_forty / count * 100).toFixed(2)
            this.info['占比在40-50'] = (forty_to_fifty / count * 100).toFixed(2)
            this.info['占比在50以上'] = (more_then_fifty / count * 100).toFixed(2)
            return res
        }

        start() {
            this.isStart = false
            this.clickEvent()
        }

        end() {
            this.isStart = true
            this.clickEvent()
        }
    }

    if (!window.fpsTool) {
        window.fpsTool = new FPS()
    }
    window.fpsTool.start()
})();