/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$(() => {
    $("#signupBtn").click(() => {
        $("#signForm").animate({
            height: [ "550px", "swing" ]
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
})