function OnLoadDesign(){
    document.getElementById("pic1_detail_block").style.display = "none";
    document.getElementById("pic2_detail_block").style.display = "none";
    document.getElementById("pic3_detail_block").style.display = "none";
    document.getElementById("pic4_detail_block").style.display = "none";
    document.getElementById("pic5_detail_block").style.display = "none";
    document.getElementById("drawing_pic2_block").style.display = "none";
    document.getElementById("drawing_pic3_block").style.display = "none";
    document.getElementById("drawing_pic4_block").style.display = "none";
    document.getElementById("drawing_pic5_block").style.display = "none";
    document.getElementById("file1_detail_block").style.display = "none";
    document.getElementById("file2_detail_block").style.display = "none";
    document.getElementById("file3_detail_block").style.display = "none";
    document.getElementById("file4_detail_block").style.display = "none";
    document.getElementById("file5_detail_block").style.display = "none";
    document.getElementById("drawing_file2_block").style.display = "none";
    document.getElementById("drawing_file3_block").style.display = "none";
    document.getElementById("drawing_file4_block").style.display = "none";
    document.getElementById("drawing_file5_block").style.display = "none";
};

function PreviewImage1(){
    var oFReader = new FileReader();
    
    oFReader.readAsDataURL(document.getElementById("drawing_pic1").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("drawing_pic1_preview").src = oFREvent.target.result;
        document.getElementById("pic1_detail_block").style.display = "block";
        document.getElementById("drawing_pic2_block").style.display = "block";
    };
};

function PreviewImage2(){
    var oFReader = new FileReader();
    
    oFReader.readAsDataURL(document.getElementById("drawing_pic2").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("drawing_pic2_preview").src = oFREvent.target.result;
        document.getElementById("pic2_detail_block").style.display = "block";
        document.getElementById("drawing_pic3_block").style.display = "block";
    };
};

function PreviewImage3(){
    var oFReader = new FileReader();
    
    oFReader.readAsDataURL(document.getElementById("drawing_pic3").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("drawing_pic3_preview").src = oFREvent.target.result;
        document.getElementById("pic3_detail_block").style.display = "block";
        document.getElementById("drawing_pic4_block").style.display = "block";
    };
};

function PreviewImage4(){
    var oFReader = new FileReader();
    
    oFReader.readAsDataURL(document.getElementById("drawing_pic4").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("drawing_pic4_preview").src = oFREvent.target.result;
        document.getElementById("pic4_detail_block").style.display = "block";
        document.getElementById("drawing_pic5_block").style.display = "block";
    };
};

function PreviewImage5(){
    var oFReader = new FileReader();
    
    oFReader.readAsDataURL(document.getElementById("drawing_pic5").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("drawing_pic5_preview").src = oFREvent.target.result;
        document.getElementById("pic5_detail_block").style.display = "block";
    };
};

function UploadFile1(){
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("drawing_file1").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("file1_detail_block").style.display = "block";
        document.getElementById("drawing_file2_block").style.display = "block";
    };
};

function UploadFile2(){
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("drawing_file2").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("file2_detail_block").style.display = "block";
        document.getElementById("drawing_file3_block").style.display = "block";
    };
};

function UploadFile3(){
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("drawing_file3").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("file3_detail_block").style.display = "block";
        document.getElementById("drawing_file4_block").style.display = "block";
    };
};

function UploadFile4(){
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("drawing_file4").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("file4_detail_block").style.display = "block";
        document.getElementById("drawing_file5_block").style.display = "block";
    };
};

function UploadFile5(){
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("drawing_file5").files[0]);
    oFReader.onload = function (oFREvent){
        document.getElementById("file5_detail_block").style.display = "block";
    };
};