/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$(() => {
    $("#signupBtn").click(() => {
        $("#signForm").animate({
            height: ["480px", "swing"]
        }, 300, function () {
            // Animation complete.
        });
        $(".slideLeftToRight").hide("slide", {direction: "left"}, 800, () => {

        });

        $(".slideRightToLeft").show("slide", {direction: "right"}, 800, () => {
            $(".slideRightToLeft").css("position", "static");
        });
    });
    $("#signinBtn").click(() => {
        $(".slideRightToLeft").hide("slide", {direction: "right"}, 800, () => {
            $(".slideRightToLeft").css("position", "absolute");
        });
        $(".slideLeftToRight").show("slide", {direction: "left"}, 800, () => {
            $("#signForm").animate({
                height: "280px"
            }, 300, function () {
                // Animation complete.
            });
        });
    });

    $("#auth").click(() => {
        WavesKeeper.publicState()
                .then(state => {
                    console.log(state);
                    $("#userName").val(state.account.name);
                    $("#publicKey").val(state.account.publicKey);
                    $("#userAddress").val(state.account.address);
                    //$("#userBalance").val(state.account.balance.available);

                }).catch(error => {
            console.error(error);
        })


    })
    $('#signup').submit(event => {
        $.ajax({
            data: $('#signup').serialize(),
            type: 'POST',
            url: '/signup'
        })
                .done((data) => {
                    console.log(data);
                    if (data.success == "1") {
                        window.location = "/home";
                    }
                });
        event.preventDefault();
    });
    $('#signin').submit(event => {
        $.ajax({
            data: $('#signup').serialize(),
            type: 'POST',
            url: '/signin',
            dataType: 'json'
        })
                .done((data) => {
                    console.log(data);
                    if (data.success == "1") {
                        window.location = "/home";
                    }
                });
        event.preventDefault();
    });
    $('#deal').submit(event => {
        $.ajax({
            data: $('#deal').serialize(),
            type: 'POST',
            url: '/newdeal',
            dataType: 'json'
        })
                .done((data) => {
                    console.log(data);
                    if (data.success == "1") {
                        window.location = "/home";
                    }
                });
        event.preventDefault();
    });
       $('#_deal').submit(event => {

        event.preventDefault();
        WavesKeeper.signAndPublishTransaction({
            type: 16,
            data: {
                fee: {
                    "tokens": "0.05",
                    "assetId": "WAVES"
                },
                dApp: '3MvqUEAdK8oa1jDS82eqYYVoHTX3S71rRPa',
                call: {
                    function: 'main',
                    args: [

                        {
                            "type": "string",
                            "value": "home1"
                        },
                        {
                            "type": "string",
                            "value": "3MyhYfrLVNe5cj191rJHxqCrR5CU7URCN8h"
                        }
                    ]
                },
                payment: [{assetId: "WAVES", tokens: 2}]
            }
        }).then((tx) => {
            console.log("Ура! Я выполнил скрипт!!!");
        }).catch((error) => {
            console.error("Что-то пошло не так", error);
        });
    });
})