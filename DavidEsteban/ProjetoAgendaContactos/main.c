#include <stdio.h>
#include <string.h>
#include <locale.h>

#define MAX_CONTACTOS 100

typedef struct{
  char nome[50];
  char apelido[50];
  char tele[50];
  char email[50];
  char obs[50];
} Contacto;

int main(){

    setlocale(LC_ALL, "Portuguese");

    Contacto agenda[MAX_CONTACTOS];

    int numContactos = 0;
    char input[200];
    int continuar = 1;

    while(continuar){
        // Menu
        printf("\n");
        printf("\n ----------------------------------------------------------------------------------------\n");
        printf("|                              Menu de Contactos                                        |\n");
        printf(" ----------------------------------------------------------------------------------------\n");
        printf("|   NC    |  Novo Contacto  (Uso: NC Nome Apelido Telefone Email Observacoes)           |\n");
        printf(" ----------------------------------------------------------------------------------------\n");
        printf("|   PC    |  Procurar Contacto (Uso: PC Nome)                                           |\n");
        printf(" ----------------------------------------------------------------------------------------\n");
        printf("|   LC    |  Listar Contactos                                                           |\n");
        printf(" ----------------------------------------------------------------------------------------\n");
        printf("|   AC    |  Atualizar Contacto (Uso: AC Nome)                                          |\n");
        printf(" ----------------------------------------------------------------------------------------\n");
        printf("|   EC    |  Eliminar Contacto (Uso: EC Nome)                                           |\n");
        printf(" ----------------------------------------------------------------------------------------\n");
        printf("|   XXX   |  Sair                                                                       |\n");
        printf(" ----------------------------------------------------------------------------------------\n");

        printf("\n> Comando:  ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0'; // REMOVER O NEW LINE

        if(strncmp(input, "NC", 2) == 0){
            if(numContactos >= MAX_CONTACTOS){
                printf("\n> Agenda cheia! <\n");
                continue;

            }

            Contacto contactoNovo;

            char observacoes[50];
            int frase = sscanf(input, "NC %s %s %s %s %[^\n]", contactoNovo.nome, contactoNovo.apelido, contactoNovo.tele, contactoNovo.email, observacoes);

            if(frase < 5){
                    system("cls");
                    printf("\n> Formato inválido. Formato: NC Nome Apelido Telefone Email Observacoes <\n");
                    continue;
            }

            // VER SE EXISTEM DUPLICADOS ----

            int existe = 0;

            for(int i = 0; i < numContactos; i++){
                if(strcmp(agenda[i].nome, contactoNovo.nome) == 0){
                    system("cls");
                    printf("\n> Já existe um contacto com o nome %s <\n", agenda[i].nome);
                    existe = 1;
                    break;
                }
            }

            if(existe) continue;

            strncpy(contactoNovo.obs, observacoes, sizeof(contactoNovo.obs) - 1);
            contactoNovo.obs[sizeof(contactoNovo.obs) - 1] = '\0';
            agenda[numContactos++] = contactoNovo;
            system("cls");
            printf("\nContacto registado com sucesso\n");
        }else if(strncmp(input, "PC", 2) == 0){

            system("cls");

            char nome[50];
            sscanf(input, "PC %49s", nome);
            printf("\nContacto a procurar: %s\n", nome);

            int encontrado = 0;

            for(int i = 0; i < numContactos; i++){
                if(strcmp(agenda[i].nome, nome) == 0){
                    printf("\nContacto encontrado: %s %s, %s, %s, %s\n", agenda[i].nome, agenda[i].apelido, agenda[i].tele, agenda[i].email, agenda[i].obs);
                    encontrado = 1;
                    break;
                }
            }
            if (encontrado==0) printf("\nContacto inexistente.\n");
        }else if(strcmp(input, "LC") == 0){
            if(numContactos == 0){
                system("cls");
                printf("\nAgenda sem contactos.\n");
            }else{
                system("cls");
                printf("\n> Contactos <\n");
                for(int i = 0; i < numContactos; i++){
                    printf("\n> [ID] %d | Nome e Apelido: %s %s, Telefone: %s, Email:%s, Obs:%s", i + 1, agenda[i].nome, agenda[i].apelido, agenda[i].tele, agenda[i].email, agenda[i].obs);
                }
            }
        }else if(strncmp(input, "AC", 2) == 0){

            char nome[50];
            sscanf(input, "AC %49s", nome);

            int encontrado = 0;

            for(int i = 0; i < numContactos; i++){

                if(strcmp(agenda[i].nome, nome) == 0){

                    encontrado = 1;

                    int opcao;

                    do{
                       system("cls");
                        printf("\n> Contacto a atualizar : %s <\n", agenda[i].nome);
                        printf("\n1 - Apelido\n2 - Telefone\n3 - Email\n4 - Observações\n5 - Sair\n");
                        printf("Escolha uma opção: ");
                        scanf("%d", &opcao);
                        getchar(); // Limpar buffer

                        switch (opcao){
                            case 1:
                                system("cls");
                                printf("> Apelido atual: %s <", agenda[i].apelido);
                                printf("\nNovo apelido: ");
                                scanf("%49s", agenda[i].apelido);
                                break;

                            case 2:
                                system("cls");
                                printf("> Telefone atual: %s <", agenda[i].tele);
                                printf("\nNovo telefone: ");
                                scanf("%49s", agenda[i].tele);
                                break;

                            case 3:
                                system("cls");
                                printf("> Email atual: %s <", agenda[i].email);
                                printf("\nNovo email: ");
                                scanf("%49s", agenda[i].email);
                                break;

                            case 4:
                                system("cls");
                                printf("> Observações atuais: %s <", agenda[i].obs);
                                printf("\nNovas observações: ");
                                getchar();
                                fgets(agenda[i].obs, sizeof(agenda[i].obs), stdin);
                                agenda[i].obs[strcspn(agenda[i].obs, "\n")] = '\0';
                                break;

                            case 5:
                                system("cls");
                                printf("\nContacto atualizado com sucesso.\n");
                                break;

                            default:
                                system("cls");
                                printf("\nOpção inválida!\n");
                        }
                    }while(opcao != 5);
                    break;
                }
            }
            if(!encontrado){
                system("cls");
                printf("\nContacto inexistente.\n");
            }
        }else if(strncmp(input, "EC", 2) == 0){

            char nome[50];
            sscanf(input, "EC %49s", nome);

            int encontrado = 0;

            for(int i = 0; i < numContactos; i++){
                if(strcmp(agenda[i].nome, nome) == 0){

                    for(int j = i; j < numContactos - 1; j++){
                        agenda[j] = agenda[j + 1];
                    }

                    numContactos--;
                    system("cls");
                    printf("\n> Contacto eliminado com sucesso <\n");
                    encontrado = 1;
                    break;

                }

            }

            if(!encontrado){
                    system("cls");
                    printf("\n> Contacto não encontrado <\n");
            }

        }else if(strcmp(input, "XXX") == 0){
            system("cls");
            printf("\nA guardar a agenda...\nSayonara!\n");
            continuar = 0;
        }else{
            system("cls");
            printf("\n> Comando inválido! <\n");
        }

    }

    return 0;

}
