// ==UserScript==
// @name         图像文字识别自动填写
// @namespace    ocr.wenz-ubuntu
// @version      0.2
// @description  获取验证码图像并自动填写识别结果
// @author       Wenz-Jam
// @match        *://*.zufe.edu.cn/*
// @grant        GM_xmlhttpRequest
// ==/UserScript==

(function() {
    'use strict';

    function processImage() {
        // 查找 class 为 "ide_code_image" 的图像
        var imageElement = document.querySelector('.ide_code_image');
        if (imageElement && imageElement.tagName === 'IMG') {
            // 获取图像的 base64 编码内容
            var imageData = imageElement.src;
            if (imageData.startsWith('data:image')) {
                console.log('找到图像');

                // 发送图像数据到后端进行文字识别
                GM_xmlhttpRequest({
                    method: 'POST',
                    url: 'http://ocr.wenz-ubuntu:8503/recognize', // 替换为你的后端地址
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: JSON.stringify({ image: imageData }),
                    onload: function(response) {
                        if (response.status === 200) {
                            // 解析 JSON 并提取 text 字段的值
                            var recognizedText = JSON.parse(response.responseText).text;
                            if (recognizedText.trim() !== '') {
                                console.log('识别结果:', recognizedText);
                                // 找到输入框并设置焦点和内容
                                var codeInput = document.querySelector('.login_box_input.code_input');
                                if (codeInput) {
                                    codeInput.focus();
                                    codeInput.value = recognizedText;

                                    // 触发输入事件
                                    var inputEvent = new Event('input', { bubbles: true });
                                    codeInput.dispatchEvent(inputEvent);
                                } else {
                                    console.error('找不到验证码输入框');
                                }
                            } else {
                                console.error('文字识别结果为空');
                            }
                        } else {
                            console.error('文字识别失败: ' + response.statusText);
                        }
                    },
                    onerror: function(error) {
                        console.error('文字识别失败: 网络错误');
                    }
                });
            } else {
                console.error('图像数据无效');
            }
        } else {
            console.log('未找到 class 为 "ide_code_image" 的图像');
        }
    }

    // 在页面加载完成后执行
    window.addEventListener('load', function() {
        processImage();
    });

    // 在 id 为 "password_login" 的按钮被点击时执行
    document.addEventListener('click', function(event) {
        if (event.target && event.target.id === 'password_login') {
            processImage();
        }
    });
})();

