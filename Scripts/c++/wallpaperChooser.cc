#include <iostream>
#include <filesystem>
#include <string>
#include <set>
#include <stdlib.h>
#include <algorithm>

using namespace std;

void prettyPrint(int index, string name){
  if(name.length() > 19){
    name = name.substr(0, 16) + "...";
  }
  int padding = 21 - name.length() - to_string(index).length();
  cout << to_string(index) + " - " + name << string(padding, ' ');
}

int main(){
  string path = "/home/odden/Pictures/";
  set<string> fileNames;


  for(auto & p : filesystem::directory_iterator(path)){
    if (!p.is_directory()){
      string filename = p.path().filename();
      string extension = filename.substr(filename.find_last_of("."));
      transform(extension.begin(), extension.end(), extension.begin(), ::tolower);
      if(extension == ".jpg" || extension == ".png"){
        fileNames.insert(filename);
      }
    }
  }

  int index = 1;
  for (string name : fileNames){
    prettyPrint(index, name);
    if (index % 3 == 0){
      cout << endl;
    }
    ++index;
  }
  cout << endl << endl << endl;

  long unsigned int choice = 0;
  while(choice == 0) {
    cout << "Please input the number of the wallpaper you want to set." << endl;
    cin >> choice;
    if (!cin || choice > fileNames.size()){
      cout << "Not a valid choice." << endl;
      choice = 0;
      cin.clear();
      cin.ignore(999, '\n');
    }
  }

  set<string>::iterator it = fileNames.begin();
  advance(it, choice -1);
  string command = "feh --bg-scale " + path + *it;
  system(command.c_str());
}
