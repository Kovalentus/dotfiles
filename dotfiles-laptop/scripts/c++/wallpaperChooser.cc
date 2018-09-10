#include <iostream>
#include <filesystem>
#include <string>
#include <set>
#include <stdlib.h>
#include <algorithm>

void pretty_print(int index, std::string name){
  if(name.length() > 19){
    name = name.substr(0, 16) + "...";
  }
  int padding = 21 - name.length() - std::to_string(index).length();
  std::cout << std::to_string(index) + " - " + name
            << std::string(padding, ' ');
}

int chooseWallpaper(const long unsigned int &highestChoice){
  long unsigned int choice = 0;
  while(choice == 0) {
    std::cout << "Please input the number of the wallpaper you want to set."
              << std::endl;
    std::cin >> choice;
    if (!std::cin || choice > highestChoice){
      std::cout << "Not a valid choice." << std::endl;
      choice = 0;
      std::cin.clear();
      std::cin.ignore(999, '\n');
    }
  }
  return choice;
}

int main(){
  std::string path = "/home/odden/Pictures/";
  std::set<std::string> fileNames;


  for(auto & p : std::filesystem::directory_iterator(path)){
    if (!p.is_directory()){
      std::string filename = p.path().filename();
      std::string extension = filename.substr(filename.find_last_of("."));
      transform(extension.begin(), extension.end(),
                extension.begin(), ::tolower);
      if(extension == ".jpg" || extension == ".png"){
        fileNames.insert(filename);
      }
    }
  }

  int index = 1;
  for (std::string name : fileNames){
    pretty_print(index, name);
    if (index % 3 == 0){
      std::cout << std::endl;
    }
    ++index;
  }
  std::cout << std::endl << std::endl << std::endl;
  int choice = chooseWallpaper(fileNames.size());

  std::set<std::string>::iterator it = fileNames.begin();
  advance(it, choice -1);
  std::string command = "feh --bg-scale \"" + path + *it + "\"";
  system(command.c_str());
}
