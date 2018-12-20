like = id => {
    console.log("ay");
  $.get("like/" + id, newlikes => {
      $("#likeicon" + id).addClass("loved");
      $("#likespan" + id).text(newlikes);
    });
    console.log('ay')
};
unlike = id => {
  $.get("/unlike/" + id, newlikes => {
      $("#likeicon" + id).removeClass("loved");
      $("#likespan" + id).text(newlikes);
    });
};
