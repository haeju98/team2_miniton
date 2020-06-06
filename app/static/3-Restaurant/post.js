function like(isLike,pk) {
  //   post 아이디를 줘야함
  $.ajax({
    cache: false,
    url: "user/like",
    data: {
      isLike: isLike,
      post_pk: pk,
    },
    type: "POST",
    success: (result) => {
      if (isLike) $("#isLike").removeClass("red");
      else $("#isLike").addClass("red");
    },
    error: function error(request, status, _error2) {
      console.log(
        "code:" +
          request.status +
          "\n" +
          "message:" +
          request.responseText +
          "\n" +
          "error:" +
          _error2
      );
    },
  });
}
