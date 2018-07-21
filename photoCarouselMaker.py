import os

if __name__ == "__main__":
    goTo = "people"
    print('<el-col :span = "12" > \
    \n    <h1 v-if = "lang == \'english\'" v-on: click = "goToPage(\'' + goTo + '\')" >People</h1 > \
    \n    <h1 v-else v-on: click = "goToPage(\'' + goTo + '\')" >Las Personas</h1 > \
    \n    <el-carousel indicator-position = "outside" >')

    photoDir = "originalImages/people/"
    for i in os.listdir(photoDir):
        # print(i)
        print('        <el-carousel-item > \
        \n            <img src = "' + photoDir + i + '" > \
        \n        </el-carousel-item >')
    print('     </el-carousel > \
        \n</el-col>')
